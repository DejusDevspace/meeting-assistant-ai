import os
from dotenv import load_dotenv
from groq import Groq
from typing import Optional
from src.settings import settings
from src.core.exceptions import AudioTranscriptionError

# Load environment variables
_ = load_dotenv()

class AudioTranscriber:
    """A class to handle audio transcription using the Whisper model from Groq."""

    # Required environment variables for audio transcription
    REQUIRED_ENV_VARS = ["GROQ_API_KEY"]

    def __init__(self):
        """Initialize the AudioTranscriber class and validate required environment variables."""
        self._validate_env_vars()
        self._client: Optional[Groq] = None

    def _validate_env_vars(self) -> None:
        """Validate required environment variables."""
        missing_vars = [var for var in self.REQUIRED_ENV_VARS if not os.getenv(var)]
        if missing_vars:
            raise ValueError(f"Required environment variables: {', '.join(missing_vars)}")

    @property
    def client(self) -> Groq:
        """Create Groq client or get client instance."""
        if self._client is None:
            self._client = Groq(api_key=settings.GROQ_API_KEY)
        return self._client

    async def transcribe(self, file_path: str) -> str:
        """Transcribe audio to text using Groq's Whisper model"""

        try:
            # Open the audio file
            with open(file_path, "rb") as audio_file:
                # Create a transcription of the audio file
                print("Transcribing audio...")
                transcription = self.client.audio.transcriptions.create(
                    file=audio_file,
                    model=settings.TRANSCRIBER_MODEL_NAME,
                    language="en",
                    response_format="text",
                )

            if not transcription:
                raise AudioTranscriptionError("No transcription data available")

            return transcription
        except Exception as e:
            raise AudioTranscriptionError(f"Audio transcription failed: {str(e)}") from e
