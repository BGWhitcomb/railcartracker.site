# app/main.py
from fastapi import FastAPI, UploadFile, File, HTTPException
import requests, json, os
from .extract import extract_pdf_data
from .schema import RailcarForm

app = FastAPI()

LOCALAI_URL = os.getenv("LOCALAI_URL", "http://localai:8080/v1/chat/completions")

def call_localai_ocr_structuring(extracted_text: str) -> dict:
    """
    Sends the OCR text to LocalAI for structured data extraction.
    """
    payload = {
        "model": "mistral",
        "messages": [
            {"role": "system", "content": "You are an expert assistant extracting structured data from OCR text on railcar inspection forms."},
            {"role": "user", "content": extracted_text}
        ],
        "temperature": 0.2
    }

    response = requests.post(LOCALAI_URL, json=payload, timeout=60)
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail=f"LocalAI error: {response.text}")

    # Extract response content
    try:
        content = response.json()["choices"][0]["message"]["content"]
        return json.loads(content)  # Convert stringified JSON into Python dict
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Invalid LocalAI response: {str(e)}")


@app.post("/extract")
async def extract_pdf(file: UploadFile = File(...)):
    temp_path = f"/app/uploads/temp_{file.filename}"
    with open(temp_path, "wb") as f:
        f.write(await file.read())

    text = extract_pdf_data(temp_path)

    structured_data = call_localai_ocr_structuring(text)
    validated = validate_localai_output(structured_data)

    return validated.dict()


def validate_localai_output(data: dict) -> RailcarForm:
    """
    Validates and normalizes LocalAI output against RailcarForm schema.
    """
    try:
        return RailcarForm(**data)
    except Exception as e:
        raise HTTPException(status_code=422, detail=f"Schema validation error: {str(e)}")
