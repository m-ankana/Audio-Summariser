import whisper

from logger import logger


def transcribe_audio(audio_path):
    """Transcribes audio using the Whisper model."""
    try:
        model = whisper.load_model("turbo")
    except Exception:
        logger.exception("Failed to load Whisper model")
        raise Exception("Failed to load Whisper model")
    try:
        logger.info("Starting transcription...")
        result = model.transcribe(audio_path)
    except Exception:
        logger.exception("Failed to transcribe audio")
        raise Exception("Failed to transcribe audio")

    return result["text"]
