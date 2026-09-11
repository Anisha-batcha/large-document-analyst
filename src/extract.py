"""
Stage 3: Text Extraction
-------------------------
Given a file path (PDF or TXT), return the raw text content.
"""

import pdfplumber


def extract_text_from_file(filepath):
    """
    Extract raw text from a PDF or TXT file.
    Returns the extracted text as a single string.
    """
    if filepath.lower().endswith(".pdf"):
        return _extract_from_pdf(filepath)
    elif filepath.lower().endswith(".txt"):
        return _extract_from_txt(filepath)
    else:
        raise ValueError("Unsupported file type. Only PDF and TXT are supported.")


def _extract_from_pdf(filepath):
    text_parts = []
    with pdfplumber.open(filepath) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text_parts.append(page_text)
    return "\n".join(text_parts)


def _extract_from_txt(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()
