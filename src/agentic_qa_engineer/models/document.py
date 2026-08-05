"""
document.py

Domain model representing a document within the Agentic QA Engineer system.

Purpose
-------
This module defines the Document model, which acts as the canonical
representation of a document after it has been ingested.

Why do we need this?
--------------------
Instead of passing dictionaries between modules, we define a strongly
typed object that represents a document throughout the application.

Benefits
--------
- Type safety
- Better IDE support
- Easier maintenance
- Consistent interface across modules
- Automatic validation through Pydantic

Lifecycle
---------
PDF
    ↓
Document
    ↓
Chunking
    ↓
Embeddings
    ↓
Retrieval
"""

from pathlib import Path
from typing import Optional

from pydantic import BaseModel, ConfigDict


class Document(BaseModel):
    """
    Represents a single source document.

    A Document object is created immediately after the ingestion
    pipeline reads a document from disk.

    This object is passed throughout the application and acts as the
    source of truth for all document-related information.

    Attributes
    ----------
    document_id
        Unique identifier for the document.

    file_name
        Name of the source document.

    file_path
        Absolute path to the document.

    content
        Complete extracted text.

    page_count
        Total number of pages.

    metadata
        Additional document metadata.
    """

    document_id: str

    file_name: str

    file_path: Path

    content: str

    page_count: int

    metadata: dict[str, str] = {}

    model_config = ConfigDict(
        arbitrary_types_allowed=True
    )