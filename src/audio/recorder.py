from dataclasses import dataclass
from datetime import datetime
import time
from pathlib import Path
from typing import Optional, Callable
import threading
import numpy as np
import sounddevice as sd
import wave
from sounddevice import CallbackFlags


@dataclass
class AudioConfig:
    """Configuration for an audio recording"""
    sample_rate: int = 44100
    channels: int = 2
    dtype: str = "int16"
    chunk_size: int = 1024
    format: str = "wav"

@dataclass
class RecordingSession:
    """Parameters for a recording session"""
    session_id: str
    start_time: datetime
    file_path: str
    duration: float = 0.0
    status: str = "created"  # Options: created, recording, paused, stopped, saved

class AudioRecorder:
    """Audio recording class to handle core recording functionalities"""

    def __init__(self, config: AudioConfig = None, output_dir: str = "data/audio/raw"):
        self.config = config or AudioConfig()
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Recording state parameters
        self.is_recording = False
        self.is_paused = False
        self.current_session: Optional[RecordingSession] = None
        self.audio_data = []
        self.recording_thread = None

        # Callbacks for recording actions
        self.on_recording_start: Optional[Callable] = None
        self.on_recording_stop: Optional[Callable] = None
        self.on_recording_pause: Optional[Callable] = None
        self.on_error: Optional[Callable] = None

    def create_session(self, session_name: str = None) -> RecordingSession:
        """Create a new recording session"""
        if session_name is None:
            session_name = f"recording_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

        # Create session ID and save path for recording
        session_id = f"{session_name}_{int(time.time())}"
        file_path = self.output_dir / f"{session_id}.{self.config.format}"

        # Create recording session object
        session = RecordingSession(
            session_id=session_id,
            start_time=datetime.now(),
            file_path=str(file_path)
        )
        return session

    def start_recording(self, session: RecordingSession = None, device_id: int = None):
        """Start recording audio"""
        if self.is_recording:
            raise RuntimeError("Recording is already in progress")

        if session is None:
            session = self.create_session()

        # Update recording state parameters
        self.current_session = session
        self.current_session.status = "recording"
        self.is_recording = True
        self.is_paused = False
        self.audio_data = []

        # Start recording in separate thread
        self.recording_thread = threading.Thread(
            target=self._record_audio,
            args=(device_id,),
            daemon=True
        )
        self.recording_thread.start()

        # if self.on_recording_start:
        #     self.on_recording_start(session)

        print(f"Recording started: {session.session_id}")
        return session

    def stop_recording(self) -> Optional[RecordingSession]:
        """Stop recording and save file"""
        if not self.is_recording:
            print("No recording in progress")
            return None

        # Update recording state parameters
        self.is_recording = False
        self.is_paused = False

        # Wait for recording thread to finish
        if self.recording_thread and self.recording_thread.is_alive():
            self.recording_thread.join(timeout=5.0)

        if self.current_session and self.audio_data:
            self._save_audio_file()
            self.current_session.status = "saved"
            self.current_session.duration = len(self.audio_data) / self.config.sample_rate

            if self.on_recording_stop:
                self.on_recording_stop(self.current_session)

            print(f"Recording stopped and saved: {self.current_session.file_path}")
            return self.current_session

        return None

    def _record_audio(self, device_id: int = None):
        """Internal method to handle audio recording"""
        try:
            def audio_callback(
                    indata: np.ndarray,
                    frames: int,
                    time_,
                    status: CallbackFlags
            ) -> None:
                if status:
                    print(f"Audio callback status: {status}")

                if not self.is_paused and self.is_recording:
                    self.audio_data.extend(indata.copy())

            # Start audio stream
            with sd.InputStream(
                    device=device_id,
                    channels=self.config.channels,
                    samplerate=self.config.sample_rate,
                    dtype=self.config.dtype,
                    callback=audio_callback,
                    blocksize=self.config.chunk_size
            ):
                print("Recording... Press Ctrl+C to stop or use stop_recording()")
                while self.is_recording:
                    time.sleep(0.1)

        except Exception as e:
            self.is_recording = False
            print("error:", e)
            if self.on_error:
                self.on_error(f"Recording error: {str(e)}")
            else:
                print(f"Recording error: {str(e)}")

    def _save_audio_file(self):
        """Save recorded audio data to file"""
        if not self.audio_data or not self.current_session:
            return

        try:
            # Convert to numpy array
            audio_array = np.array(self.audio_data, dtype=self.config.dtype)

            # Save as WAV file
            with wave.open(self.current_session.file_path, 'wb') as wav_file:
                wav_file.setnchannels(self.config.channels)
                wav_file.setsampwidth(2)  # 16-bit audio
                wav_file.setframerate(self.config.sample_rate)
                wav_file.writeframes(audio_array.tobytes())

            print(f"Audio saved to: {self.current_session.file_path}")

        except Exception as e:
            error_msg = f"Error saving audio file: {str(e)}"
            print("error:", error_msg)
            if self.on_error:
                self.on_error(error_msg)
            else:
                print(error_msg)
