from datetime import datetime
import time
from src.audio import AudioRecorder
from src.audio.utils import validate_audio_file
from src.modules.transcription import AudioTranscriber
import asyncio


def on_start(session):
    print(f"Recording started: {session.session_id}")


def on_stop(session):
    print(f"Recording saved: {session.file_path}")
    print(f"Duration: {session.duration:.2f} seconds")

async def main():
    print("Hello from meeting-assistant-app!")

    # print("Available audio devices:")
    # devices = sd.query_devices()
    # for i, device in enumerate(devices):
    #     if device['max_input_channels'] > 0:
    #         print(f"{i}: {device['name']} (Input channels: {device['max_input_channels']})")
    # print("\nNumber of available audio devices:", len(devices))

    transcriber = AudioTranscriber()
    recorder = AudioRecorder(output_dir="src/data/audio/raw")
    recorder.on_recording_start = on_start
    recorder.on_recording_stop = on_stop

    # Example recording workflow
    try:
        print(print("\nStarting 5-second test recording..."))
        session = recorder.start_recording()

        # Record for 5 seconds
        time.sleep(5)

        final_session = recorder.stop_recording()

        if final_session:
            print(f"\nRecording completed!")
            print(f"File: {final_session.file_path}")
            print(f"Duration: {final_session.duration:.2f} seconds")
            print(f"Valid file: {validate_audio_file(final_session.file_path)}")

        transcription = await transcriber.transcribe(final_session.file_path)
        print("\n\nAudio transcription:\n {}".format(transcription))


    except KeyboardInterrupt:
        print("\nRecording interrupted by user")
        recorder.stop_recording()
    except Exception as e:
        print(f"Error during recording: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())
