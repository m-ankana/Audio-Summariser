# import os
# import shutil

# from fastapi import FastAPI, File, Request, UploadFile
# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates

# from audio_to_text.transcribe import transcribe_audio
# from logger import logger
# from text_processing.summarizer import summarize_text

# app = FastAPI()
# templates = Jinja2Templates(directory="templates")

# UPLOAD_FOLDER = "uploads"
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# @app.get("/", response_class=HTMLResponse)
# def index(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request, "summary": ""})


# @app.post("/", response_class=HTMLResponse)
# def summarize(request: Request, file: UploadFile = File(...)):
#     if not file.filename:
#         return templates.TemplateResponse(
#             "index.html", {"request": request, "summary": "Error: No file selected"}
#         )
#     ext = os.path.splitext(file.filename)[1].lower()
#     if ext not in {".wav", ".mp3", ".m4a", ".flac"}:
#         return templates.TemplateResponse(
#             "index.html",
#             {"request": request, "summary": "Error: Only audio files are allowed"},
#         )

#     file_path = os.path.join(UPLOAD_FOLDER, file.filename)
#     file_path = os.path.join(UPLOAD_FOLDER, file.filename)
#     try:
#         # Save uploaded file
#         with open(file_path, "wb") as f:
#             shutil.copyfileobj(file.file, f)

#         logger.info("Received file: %s", file.filename)
#         text = transcribe_audio(file_path)
#         summary = summarize_text(text)

#         return templates.TemplateResponse(
#             "index.html", {"request": request, "summary": summary}
#         )
#     except Exception as e:
#         logger.exception("Error during summarization")
#         return templates.TemplateResponse(
#             "index.html", {"request": request, "summary": f"Error: {e}"}
#         )

import os
import shutil

from fastapi import FastAPI, File, Request, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from audio_to_text.transcribe import transcribe_audio
from logger import logger
from text_processing.summarizer import summarize_text

# FastAPI app
app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Upload folder (create if missing)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Allowed audio extensions
ALLOWED_EXTENSIONS = {".wav", ".mp3", ".m4a", ".flac"}


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "summary": ""})


@app.post("/", response_class=HTMLResponse)
def summarize(request: Request, file: UploadFile = File(...)):
    # Ensure filename exists
    if not file.filename:
        return templates.TemplateResponse(
            "index.html", {"request": request, "summary": "Error: No file selected"}
        )

    # Check file extension
    ext = os.path.splitext(file.filename)[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        return templates.TemplateResponse(
            "index.html",
            {"request": request, "summary": "Error: Only audio files are allowed"},
        )

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    try:
        # Save uploaded file
        with open(file_path, "wb") as f:
            shutil.copyfileobj(file.file, f)

        logger.info("Received file: %s", file.filename)

        # Run pipeline
        text = transcribe_audio(file_path)
        summary = summarize_text(text)

        return templates.TemplateResponse(
            "index.html", {"request": request, "summary": summary}
        )
    except Exception as e:
        logger.exception("Error during summarization")
        return templates.TemplateResponse(
            "index.html", {"request": request, "summary": f"Error: {e}"}
        )
