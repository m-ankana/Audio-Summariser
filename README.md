
# Audio Summarizer 🎧📝

A simple end-to-end application that takes an audio file as input, transcribes it to text, and generates a concise summary using a text summarization model.

Built with **FastAPI**, designed for clarity, modularity, and easy deployment.

---

## ✨ Features

- Upload audio files via a minimal web UI
- Automatic speech-to-text transcription
- Text summarization
- Server-side validation for audio files
- Logging to terminal and `.log` file
- Deployed without Docker using Render

---

## 🧠 Architecture

The system has two main components:

1. **Audio → Text**
   - Transcribes uploaded audio files into text
2. **Text → Summary**
   - Generates a concise summary from the transcript

Each component lives in its own module and is composed together via a FastAPI application.

---

## 🗂️ Project Structure

```

audio_summarizer/
├── app.py                 # FastAPI entrypoint
├── audio_to_text/
│   └── transcribe.py
├── text_processing/
│   └── summarizer.py
├── templates/
│   └── index.html
├── logger.py
├── uploads/               # Temporary audio uploads (ignored by git)
├── requirements.txt
├── README.md

````

---

## 🚀 Running Locally

### 1. Clone the repository

```bash
git clone git@github.com:m-ankana/Audio-Summariser.git
cd Audio-Summariser
````

### 2. Create and activate a virtual environment

```bash
python -m venv env
source env/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the server

```bash
uvicorn app:app --reload
```

Visit:
👉 `http://127.0.0.1:8000`

---


## ⚠️ Notes & Limitations

* Uploaded audio files are stored temporarily and cleared on redeploy
* Large audio files may increase processing time
* Designed as a single-user demo application (no authentication)

---

## 🔮 Future Improvements

* Progress indicator for long audio files
* Support for multiple languages
* Persistent storage (e.g. S3)
* Authentication and user accounts
* Batch uploads

---

## 🧩 Motivation

This project was built to understand:

* End-to-end ML system integration
* Backend engineering best practices
* FastAPI-based UI workflows

---

## 🧑‍💻 Author

**Ankana Mukherjee**
