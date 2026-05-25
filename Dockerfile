# 1. Base image (stable, ML-friendly)
FROM python:3.10-slim

# 2. Prevent Python from writing .pyc files & buffering logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Set work directory
WORKDIR /app

# 4. Install system dependencies (important for audio + whisper)
RUN apt-get update && apt-get install -y \
    ffmpeg \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 5. Copy requirements first (Docker layer caching)
COPY requirements.txt .

# 6. Install Python dependencies
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# 7. Copy the rest of the code
COPY . .

# 8. Expose port (FastAPI default)
EXPOSE 8000

# 9. Run the app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
