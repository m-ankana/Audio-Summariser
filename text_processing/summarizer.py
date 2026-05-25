
# import ollama

# from logger import logger


# def summarize_text(text):
#     """Summarizes text using the Ollama model."""
#     try:
#         logger.info("Starting summarization...")

#         prompt = f"Give a short summary for the following conversation. Highlight the key points. Conversation:{text}"

#         response = ollama.chat(
#             model="qwen2.5:1.5b", messages=[{"role": "user", "content": prompt}]
#         )
#     except Exception:
#         logger.exception("Failed to start summarization")
#         raise Exception("Failed to start summarization")

#     return response["message"]["content"]
import os

from dotenv import load_dotenv
from openai import OpenAI

from logger import logger

load_dotenv()

client = OpenAI()


def summarize_text(text):
    """Summarizes text using OpenAI chat model."""
    try:
        logger.info("Starting summarization...")

        prompt = (
            "Give a short summary for the following conversation. "
            "Highlight the key points.\n\n"
            f"Conversation:\n{text}"
        )

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that summarizes conversations clearly and concisely.",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=0.3,  # low temperature for consistent summaries
        )

        summary = response.choices[0].message.content

    return summary
