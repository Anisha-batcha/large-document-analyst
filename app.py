"""
Large Document Analyst
-----------------------
A RAG (Retrieval-Augmented Generation) system that lets a user upload
large documents (legal contracts, research papers, financial reports)
and ask questions about them in plain English.

Stage 1: Basic Flask app skeleton — confirms the server runs.
Later stages will add: upload, text extraction, chunking, embeddings,
vector search, and LLM-based answer generation.
"""

import os
from flask import Flask, render_template, request
from src.extract import extract_text_from_file

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"pdf", "txt"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


def allowed_file(filename):
    """Only accept .pdf and .txt files."""
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_file():
    if "document" not in request.files:
        return render_template("index.html", message="No file part in the request.")

    file = request.files["document"]

    if file.filename == "":
        return render_template("index.html", message="No file selected.")

    if file and allowed_file(file.filename):
        save_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(save_path)

        # Stage 3: extract text right after saving
        extracted_text = extract_text_from_file(save_path)
        preview = extracted_text[:500] + ("..." if len(extracted_text) > 500 else "")

        return render_template(
            "index.html",
            message=f"'{file.filename}' uploaded and text extracted! "
                     f"({len(extracted_text)} characters found) — Stage 3 complete",
            preview=preview
        )
    else:
        return render_template("index.html", message="Only PDF or TXT files are allowed.")


if __name__ == "__main__":
    app.run(debug=True)
