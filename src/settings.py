from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
        env_file_encoding="utf-8"
    )

    GROQ_API_KEY: str
    TRANSCRIBER_MODEL_NAME: str = "whisper-large-v3-turbo"
    AUDIO_RECORDING_DEFAULT_PATH = str = "data/audio/raw"

settings = Settings()
