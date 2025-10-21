# form_etl

Python FastAPI OCR/ETL service.

Prerequisites
- Python 3.10+ (match requirements.txt)
- pip

Dev and run
```bash
cd form_etl
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

Notes
- OCR logic in `app/ocr.py`, extraction pipeline in `app/extract.py`.
- Sample PDFs in `sample_pdf/`.
- Docker build:
```bash
docker build -t form_etl -f Dockerfile .
```