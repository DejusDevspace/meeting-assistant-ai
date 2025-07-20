import os
from groq import Groq
from typing import Optional
from src.settings import settings


class AudioTranscriber:
    """A class to handle audio transcription using the Whisper model from Groq."""

    # Required environment variables for audio transcription
    REQUIRED_ENV_VARS = ["GROQ_API_KEY"]

    def __init__(self):
        """Initialize the AudioTranscriber class and validate required environment variables."""
        self._validate_env_vars()
        self._client = Optional[Groq]

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
