# 📝 Project Report: RAG-based Digital Twin

> **Note:** You may also submit this report separately as a `.docx` or `.pdf`.

> **Note:** Below is a suggested template of what to include in your report. This is not a comprehensive list—please document and justify all your design decisions. Also feel free to skip anything from the suggested template if not relevant.


---

## 1. Data Exploration

- **Input Format:** Describe the documents provided (e.g., PDF, TXT).
- **Structure Observations:** Note any patterns (point of view, speech patterns)
- **Parsing Tools Used:** e.g., `PyMuPDF`, `pdfplumber`, `langchain.document_loaders`.

---

## 2. Text Chunking Strategy

- **Chunking Method:** e.g., RecursiveCharacterTextSplitter
- **Chunk Size & Overlap:** Justify the values chosen (e.g., 500 chars, 100 overlap).
- **Why this matters:** Explain how chunk size impacts semantic recall & latency.

---

## 3. Vector Store + Embeddings

- **Embedding Model:** e.g., `OpenAIEmbeddings`, `Instructor`, etc.
- **Vector Store Chosen:** e.g., `FAISS`, `Chroma`, `Pinecone`
- **Justification:** Why this setup was selected (speed, scale, simplicity, etc.)

---

## 4. Retrieval-Augmented Generation (RAG)

- **Retrieval Strategy:** Top-K search, filtering, etc.
- **LLM Used:** e.g., `gpt-3.5-turbo`
- **How RAG is wired:** Describe flow: `query → context → prompt → response`.

---

## 5. Persona Modeling

- **Technique Used:** Prompt engineering / fine-tuning
- **Prompt Template Example:**  
  ```plaintext
  You are [customer name]. Use the following context to respond like them...

## 6. Design Descisions and Tradeoffs

- **Tool Choices:** 
- **Latency vs Accuracy:** 
- etc.
