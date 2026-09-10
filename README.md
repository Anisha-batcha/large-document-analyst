# Large Document Analyst

A Retrieval-Augmented Generation (RAG) system that lets you upload large
documents — legal contracts, research papers, financial reports — and
ask questions about them in plain English, getting answers grounded in
the actual document content.

## Tech Stack
- **Backend:** Python, Flask
- **Text Extraction:** pdfplumber
- **Embeddings:** sentence-transformers
- **Vector Search:** FAISS
- **Answer Generation:** Hugging Face Inference API
- **Frontend:** HTML/CSS

## Project Status
- [x] Stage 1: Project setup
- [ ] Stage 2: Document upload
- [ ] Stage 3: Text extraction
- [ ] Stage 4: Text chunking
- [ ] Stage 5: Embedding generation
- [ ] Stage 6: Vector database integration
- [ ] Stage 7: Semantic retrieval
- [ ] Stage 8: LLM-based answer generation (full RAG pipeline)
- [ ] Stage 9: Frontend UI
- [ ] Stage 10: Error handling + documentation polish

## Setup
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```
Visit `http://127.0.0.1:5000` in your browser.

## How It Works (RAG Pipeline)
1. User uploads a document.
2. Document text is extracted and split into chunks.
3. Each chunk is converted into a vector embedding.
4. When the user asks a question, it's also embedded and matched
   against the stored chunks to find the most relevant ones.
5. The relevant chunks + question are sent to an LLM, which generates
   a grounded answer.
