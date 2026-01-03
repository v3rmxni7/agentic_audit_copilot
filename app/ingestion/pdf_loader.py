import pdfplumber
from typing import List

def load_pdf_text(file_path: str) -> List[str]:
    pages = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                pages.append(text)
    return pages
