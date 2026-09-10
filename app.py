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

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Large Document Analyst is running! Stage 1 complete."


if __name__ == "__main__":
    app.run(debug=True)
