from langchain_groq import ChatGroq
from src.settings import settings

def get_summary_model(temperature: float = 0.5) -> ChatGroq:
    return ChatGroq(
        api_key=settings.GROQ_API_KEY,
        model=settings.SUMMARIZER_MODEL_NAME,
        temperature=temperature
    )
