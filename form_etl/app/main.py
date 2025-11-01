from fastapi import FastAPI, UploadFile, File
from .extract import extract_pdf_data
from .localai import call_localai_ocr_structuring, parse_and_validate_railcar_form as validate_localai_output

app = FastAPI()

@app.post("/extract")
async def extract_pdf(file: UploadFile = File(...)):
    temp_path = f"/app/uploads/temp_{file.filename}"
    with open(temp_path, "wb") as f:
        f.write(await file.read())

    text = extract_pdf_data(temp_path)

    structured_data = call_localai_ocr_structuring(text)
    validated = validate_localai_output(structured_data)

    return validated.dict()


@app.get("/")
async def root():
    return {"message": "Railcar Form ETL Service is running."}
