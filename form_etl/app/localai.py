import os, json, requests
from fastapi import HTTPException
from pydantic import ValidationError
from .schema import RailcarForm

LOCALAI_URL = os.getenv("LOCALAI_URL", "http://localai:8081/v1/chat/completions")

def call_localai_ocr_structuring(extracted_text: str) -> dict:
    """
    Sends the OCR text to LocalAI for structured data extraction.
    """
    response = requests.post(LOCALAI_URL, json={
        "model": "c4ai-command-r7b-12-2024",
        "messages": [
            {"role": "system", "content": "You are an expert assistant extracting structured data from OCR text on railcar inspection forms."},
            {"role": "user", "content": extracted_text}
        ],
        "temperature": 0.2,
        "max_tokens": 1000,
        "timeout": 60
    })

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail=f"LocalAI error: {response.text}")

    # Extract response content
    try:
        content = response.choices[0].message.content
        return json.loads(content)  # Convert stringified JSON into Python dict
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Invalid LocalAI response: {str(e)}")
    

def parse_and_validate_railcar_form(data: dict) -> RailcarForm:
    """
    Parses and validates LocalAI output against RailcarForm schema.
    """
    try:
        return RailcarForm(**data)
    except ValidationError as e:
        error_detail = f"Schema validation error: {str(e)} | Field errors: {e.errors()}"
        raise HTTPException(status_code=422, detail=error_detail)


def process_railcar_form(extracted_text: str) -> RailcarForm:
    """
    Main function to process extracted OCR text and return validated RailcarForm data.
    """
    localai_output = call_localai_ocr_structuring(extracted_text)
    railcar_form = parse_and_validate_railcar_form(localai_output)
    return railcar_form