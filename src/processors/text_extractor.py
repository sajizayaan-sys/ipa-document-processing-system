from pathlib import Path
from pypdf import PdfReader


def extract_text_from_file(file_path: Path) -> str:
    """
    Extract text from a supported document.
    Currently supports:
    - .txt
    - .pdf
    """

    if file_path.suffix.lower() == ".txt":
        return file_path.read_text(encoding="utf-8", errors="ignore")

    if file_path.suffix.lower() == ".pdf":
        reader = PdfReader(file_path)
        text = ""

        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"

        return text

    return ""
