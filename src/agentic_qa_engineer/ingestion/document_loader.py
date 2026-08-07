"""
document_loader.py

Generic document loader for the Agentic QA Engineer.

Purpose
-------
This module provides a unified entry point for loading documents
into the application.

Why do we need this?
--------------------
Today the application only supports PDF documents.

In the future we may support:

- DOCX
- Markdown
- HTML
- Plain Text

The rest of the application should not know which loader is being
used. It should simply request a Document.

This follows the Open/Closed Principle:

Open for extension.
Closed for modification.

Future loaders can be added without changing downstream modules.

Current Supported Formats
-------------------------

- PDF

Future Formats
--------------

- DOCX
- HTML
- Markdown
- TXT
"""

from pathlib import Path

from agentic_qa_engineer.ingestion.pdf_loader import PDFLoader
from agentic_qa_engineer.models import Document


class DocumentLoader:
    """
    Generic document loader.

    This class delegates the loading process to the appropriate
    document loader based on the file type.

    Currently only PDF documents are supported.
    """

    def __init__(self) -> None:
        """
        Initialize the available document loaders.
        """

        self._pdf_loader = PDFLoader()

    def load(self, file_path: Path) -> Document:
        """
        Load a document from disk.

        Parameters
        ----------
        file_path : Path
            Path to the source document.

        Returns
        -------
        Document
            Parsed document.

        Raises
        ------
        ValueError
            If the document type is unsupported.
        """

        suffix = file_path.suffix.lower()

        if suffix == ".pdf":
            return self._pdf_loader.load(file_path)

        raise ValueError(
            f"Unsupported document type: {suffix}"
        )