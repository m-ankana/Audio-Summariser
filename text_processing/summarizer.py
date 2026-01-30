import ollama

from logger import logger


def summarize_text(text):
    """Summarizes text using the Ollama model."""
    try:
        logger.info("Starting summarization...")

        prompt = f"Give a short summary for the following conversation. Highlight the key points. Conversation:{text}"

        response = ollama.chat(
            model="qwen2.5:1.5b", messages=[{"role": "user", "content": prompt}]
        )
    except Exception:
        logger.exception("Failed to start summarization")
        raise Exception("Failed to start summarization")

    return response["message"]["content"]
