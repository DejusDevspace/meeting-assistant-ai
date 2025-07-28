from src.core.prompts import SUMMARIZER_PROMPT_V2
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from helpers import get_summary_model
from langchain_groq import ChatGroq

def get_transcript_summary_chain(model: ChatGroq, transcript: str):
    system_message = SUMMARIZER_PROMPT_V2
    # Add transcript to system message for processing
    system_message += f"\n\nTranscript of the meeting the user just attended: {transcript}"

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_message),
            MessagesPlaceholder(variable_name="transcript")
        ]
    )

    return prompt | model

