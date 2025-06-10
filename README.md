# Dolly's Digital Twin

A Streamlit-based chat application that serves as a digital twin for Dolly, capable of answering user queries embodying the persona of dolly using RAG (Retrieval-Augmented Generation).

## Project Structure

```
.
├── app.py                          # Main Streamlit application
├── requirements.txt                # Project dependencies
├── DataExtractionAndSave.ipynbv    # Data Extraction and Storage into vectorDB (TODO)
└── utils/
    ├── rag.py         # RAG implementation (TODO)
    ├── llm.py         # LLM integration (TODO)
    └── prompt.py      # Prompt templates and system messages (TODO)
```

## TODOs

### 1. Data Extraction and Storage (`DataExtractionAndSave.ipynb`)
- Load PDF and TXT data
- Explore data to determine chunking / storage strategies and extracting speech pattern
- Store data into the vectorDB

### 2. RAG Implementation (`utils/rag.py`)
- Set up vector store connection and configuration
- Implement document storage in vector store
- Implement context retrieval based on user queries

### 3. LLM Integration (`utils/llm.py`)
- Implement actual LLM API calls passing in relevant context
- Handle data retireved from vector store
- Handle chat history

### 4. Prompt Engineering (`utils/prompt.py`)
- Refine system prompt for better responses
- Implement other required prompts

### 5. Feel free to add any other folders/ files as you see fit

## Getting Started

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
streamlit run app.py
```

## Current Features
- Basic chat interface with message history
- Placeholder RAG and LLM implementations

## Next Steps
1. Implement document processing pipeline 
2. Implement vector store integration
3. Add actual LLM API calls
4. Refine prompt engineering

## Deliverables
1. DataExtractionAndSave.ipynb, rag.py, llm.py, prompt.py
2. requiremnts.txt
3. report (formats: .md / .txt /.pdf)
4. Functioning app.py with replies mimicing the persona from the documents 

