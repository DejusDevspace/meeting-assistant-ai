import os
from dotenv import load_dotenv
from groq import Groq
from src.settings import settings
from typing import Optional

# Load environment variables
_ = load_dotenv()

class Summarizer:
    """A class to create summaries of transcribed audio to capture key points."""

    # Required environment variables for text summarization
    REQUIRED_ENV_VARS = ["GROQ_API_KEY"]

    def __init__(self):
        """Initialize the Summarizer class and validate required environment variables."""
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

    async def summarize(self, text: str) -> str:
        pass
    