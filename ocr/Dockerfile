# Dockerfile（最小例）
FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y poppler-utils tesseract-ocr && \
    pip install --no-cache-dir paddleocr pdf2image

WORKDIR /app
COPY . /app
CMD ["python", "ocr_main.py", "sample.pdf"]