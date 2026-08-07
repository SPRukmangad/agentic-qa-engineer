"""
pdf_loader.py

PDF ingestion module for the Agentic QA Engineer.

Purpose
-------
This module is responsible for loading PDF documents from disk and
converting them into the application's Document domain model.

Why do we need this?
--------------------
The RAG pipeline operates on structured Document objects rather than
raw PDF files.

This loader acts as the first stage of the ingestion pipeline.

Pipeline
--------
PDF File
    │
    ▼
PyMuPDF
    │
    ▼
Extract Text + Metadata
    │
    ▼
Document Model

Why PyMuPDF?
------------
PyMuPDF was selected because it offers:

- Fast PDF parsing
- High-quality text extraction
- Metadata support
- Active maintenance
- Excellent performance on large PDFs

Trade-offs
----------
Pros
- Very fast
- Easy API
- Good extraction quality
- Suitable for production workloads

Cons
- Does not perfectly preserve tables
- Scanned PDFs require OCR (future enhancement)

Future Improvements
-------------------
- OCR support
- DOCX loader
- HTML loader
- Markdown loader
"""

from pathlib import Path
from uuid import uuid4  #Globally unique file id

import fitz  # PyMuPDF

from agentic_qa_engineer.models import Document


class PDFLoader:
    """
    Loads PDF documents into the application's Document model.

    This class is responsible only for PDF parsing.

    It does NOT:

    - Chunk documents
    - Generate embeddings
    - Store vectors

    Those responsibilities belong to later stages of the pipeline.
    """

    def load(self, file_path: Path) -> Document:
        """
        Load a PDF document from disk.

        Parameters
        ----------
        file_path : Path
            Path to the PDF document.

        Returns
        -------
        Document
            Parsed document object.

        Raises
        ------
        FileNotFoundError
            If the PDF file does not exist.

        RuntimeError
            If the PDF cannot be opened.
        """

        if not file_path.exists():
            raise FileNotFoundError(
                f"PDF file not found: {file_path}"
            )

        with fitz.open(file_path) as pdf:
            pages = []

            for page in pdf:
                pages.append(page.get_text())

            content = "\n".join(pages)

            metadata = pdf.metadata or {}

            return Document(
                document_id=str(uuid4()),
                file_name=file_path.name,
                file_path=file_path.resolve(),
                content=content,
                page_count=len(pdf),
                metadata={
                    "title": metadata.get("title", ""),
                    "author": metadata.get("author", ""),
                    "creator": metadata.get("creator", ""),
                    "producer": metadata.get("producer", ""),
                },
            )