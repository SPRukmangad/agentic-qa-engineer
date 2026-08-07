"""
chunk.py

Domain model representing a document chunk.

Purpose
-------
This module defines the DocumentChunk model, which represents the
smallest searchable unit in the RAG pipeline.

Why do we need this?
--------------------
Large documents cannot be embedded effectively as a single block of
text. They must first be divided into smaller semantic chunks.

Each chunk is embedded independently and stored in the vector database.

Benefits
--------
- Consistent data representation
- Easier retrieval
- Better embedding quality
- Fine-grained citations
- Strong typing through Pydantic
"""

from pydantic import BaseModel, ConfigDict


class DocumentChunk(BaseModel):
    """
    Represents a single chunk extracted from a document.

    Attributes
    ----------
    chunk_id
        Unique identifier for the chunk.

    document_id
        Identifier of the parent document.

    chunk_index
        Sequential position of the chunk within the document.

    page_number
        Source page number.

    content
        Text contained in the chunk.

    metadata
        Additional chunk metadata.
    """

    chunk_id: str

    document_id: str

    chunk_index: int

    page_number: int

    content: str

    metadata: dict[str, str] = {}

    model_config = ConfigDict(
        extra="forbid"
    )