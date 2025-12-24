from pathlib import Path
import pdfplumber
import logging

def extract_text_from_pdf(pdf_path: Path) -> str:
    text_chunks = []

    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page_number, page in enumerate(pdf.pages, start=1):
                page_text = page.extract_text()
                if page_text:
                    text_chunks.append(
                        f"\n--- Page {page_number} ---\n{page_text}"
                    )

        logging.info(f"Extracted text from PDF: {pdf_path.name}")

    except Exception as e:
        logging.error(f"PDF extraction failed ({pdf_path.name}): {e}")
        return ""

    return "\n".join(text_chunks)
