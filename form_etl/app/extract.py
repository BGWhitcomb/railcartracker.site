import fitz
from .ocr import extract_handwritten_text

def extract_pdf_data(pdf_path: str) -> str:
    doc = fitz.open(pdf_path)
    structured_text = ""
    
    for page in doc:
        structured_text += page.get_text()
    
    doc.close()
    handwritten_text = extract_handwritten_text(pdf_path)
    combined_text = f"{structured_text}\n\n# OCR Layer\n{handwritten_text}"
    return combined_text