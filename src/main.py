from processors.text_extractor import extract_text_from_file

from pathlib import Path
from datetime import datetime

# Define directories
BASE_DIR = Path(__file__).resolve().parent
INPUT_DIR = BASE_DIR / "input"
OUTPUT_DIR = BASE_DIR / "output"

# Create directories if they don't exist
INPUT_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

def process_files():
    results = []

    for file in INPUT_DIR.iterdir():
        if file.is_file():
            text = extract_text_from_file(file)

            info = {
                "filename": file.name,
                "size_bytes": file.stat().st_size,
                "text_length": len(text),
            } 


            results.append(info)

    return results

def generate_report(results):
    report_path = OUTPUT_DIR / "report.txt"
    with report_path.open("w", encoding="utf-8") as f:
        for item in results:
            f.write(
                f"File: {item['filename']} | "
                f"Size: {item['size_bytes']} bytes | "
                f"Text length: {item['text_length']} characters\n"
            )

    return report_path

if __name__ == "__main__":
    data = process_files()
    report = generate_report(data)
    print(f"Processed {len(data)} files.")
    print(f"Report saved to: {report}")

