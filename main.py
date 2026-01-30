from audio_to_text.transcribe import transcribe_audio
from logger import logger
from text_processing.summarizer import summarize_text


def main(audio_file: str):
    logger.info("Starting transcription for %s", audio_file)
    text = transcribe_audio(audio_file)
    logger.info("Transcription complete. Text length: %d characters", len(text))

    logger.info("Starting summarization...")
    summary = summarize_text(text)
    logger.info("Summarization complete.")

    logger.info("Summary:\n%s", summary)


if __name__ == "__main__":
    audio_file_path = "/Users/ankana/Desktop/Audio summariser /Pathir.m4a"
    main(audio_file_path)
