import wave

def get_audio_duration(file_path: str) -> float:
    """Get the duration of an audio file in seconds"""
    try:
        with wave.open(file_path, 'rb') as wav_file:
            frames = wav_file.getnframes()
            sample_rate = wav_file.getframerate()
            duration = frames / float(sample_rate)
            return duration
    except Exception as e:
        print(f"Error getting audio duration: {str(e)}")
        return 0.0


def validate_audio_file(file_path: str) -> bool:
    """Validate if audio file is readable and not corrupted"""
    try:
        with wave.open(file_path, 'rb') as wav_file:
            # Try to read basic properties
            channels = wav_file.getnchannels()
            sample_rate = wav_file.getframerate()
            frames = wav_file.getnframes()

            # Basic properties validation
            if channels < 1 or sample_rate < 1000 or frames < 1:
                return False

            return True
    except Exception:
        return False
