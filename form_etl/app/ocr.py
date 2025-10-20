from paddleocr import PaddleOCR
from pdf2image import convert_from_path

ocr = PaddleOCR(use_angle_cls=True, lang='en')

def extract_handwritten_text(pdf_path: str) -> str:
    images = convert_from_path(pdf_path, dpi=300)
    text_blocks = []

    for page in images:
        result = ocr.ocr(page)
        if result and result[0]:  # Check if result is not empty
            for line in result:
                for item in line:
                    bbox, (text, confidence) = item
                    if confidence > 0.5:
                        text_blocks.append(text)
    return "\n".join(text_blocks)
