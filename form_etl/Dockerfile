FROM python:3.11-slim

WORKDIR /app

# Install system dependencies required by OpenCV, PaddleOCR, and PDF processing
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    swig \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 \
    libgl1 \
    libgomp1 \
    poppler-utils \
    tesseract-ocr \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --prefer-binary -r requirements.txt

# Copy the rest of the ETL source
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Run FastAPI with uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
