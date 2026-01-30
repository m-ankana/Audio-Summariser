import logging

logger = logging.getLogger("audio_summarizer")
logger.setLevel(logging.INFO)

# Formatter (shared by all handlers)
formatter = logging.Formatter(
    "%(asctime)s [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)

# Handler 1: StreamHandler for terminal
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

# Handler 2: FileHandler for .log file
file_handler = logging.FileHandler("app.log", mode="w")  # overwrite each run
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

# Add handlers to logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)
