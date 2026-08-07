"""
Document ingestion package.

This package contains all modules responsible for loading documents
into the Agentic QA Engineer application.

Responsibilities
----------------
- Read documents from disk
- Support multiple document formats
- Convert source files into the application's Document domain model

Currently Supported Formats
---------------------------
- PDF

Future Supported Formats
------------------------
- DOCX
- Markdown
- HTML
- Plain Text

Public API
----------
The rest of the application should import only from this package,
rather than individual implementation modules.

Example
-------

from agentic_qa_engineer.ingestion import DocumentLoader
"""

from .document_loader import DocumentLoader
from .pdf_loader import PDFLoader

__all__ = [
    "DocumentLoader",
    "PDFLoader",
]