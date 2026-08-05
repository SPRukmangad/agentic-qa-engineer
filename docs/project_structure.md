# Project Structure

```
agentic-qa-engineer/

│
├── docs/
│
├── logs/
│
├── src/
│   └── agentic_qa_engineer/
│       │
│       ├── config/
│       ├── logging/
│       ├── models/
│       ├── ingestion/
│       ├── chunking/
│       ├── embeddings/
│       ├── vectordb/
│       ├── retrieval/
│       ├── prompts/
│       ├── llm/
│       ├── memory/
│       ├── agents/
│       ├── evaluation/
│       ├── api/
│       └── utils/
│
├── tests/
│
├── .env
├── .gitignore
├── pyproject.toml
└── README.md
```

---

# Directory Responsibilities

## docs/

Project documentation.

Contains

- Architecture
- Design decisions
- Sprint logs
- Roadmap
- Blueprint

---

## logs/

Application log files.

Ignored by Git.

---

## config/

Application configuration.

Contains

- Settings
- Environment configuration

---

## logging/

Centralized logging module.

Every module imports logging from here.

---

## models/

Application data models.

Examples

- Document
- Chunk
- RetrievalResult

---

## ingestion/

Responsible for reading documents.

---

## chunking/

Responsible for splitting text into chunks.

---

## embeddings/

Responsible for embedding generation.

---

## vectordb/

Vector database implementation.

---

## retrieval/

Search and retrieval pipeline.

---

## prompts/

Prompt templates.

---

## llm/

LLM integration layer.

---

## memory/

Conversation and agent memory.

---

## agents/

LangGraph workflows.

---

## evaluation/

Evaluation metrics.

---

## api/

FastAPI endpoints.

---

## utils/

Shared helper functions.

---

## tests/

Unit and integration tests.

---

# Folder Design Principles

- One responsibility per folder
- High cohesion
- Low coupling
- Easy testing
- Easy extension