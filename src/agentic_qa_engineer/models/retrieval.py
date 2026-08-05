"""
retrieval.py

Domain model representing a retrieval result.

Purpose
-------
This module defines the RetrievalResult model, which represents
a single result returned from the retrieval pipeline.

Why do we need this?
--------------------
After performing semantic search against the vector database,
the application needs a consistent way to represent each retrieved
document chunk.

Instead of passing dictionaries throughout the application, we
use a strongly typed model that acts as a contract between the
retriever, prompt builder, and LLM.

Benefits
--------
- Type safety
- Consistent interface
- Easier debugging
- Better maintainability
- Supports citations and relevance scores

Lifecycle
---------
User Query
    ↓
Retriever
    ↓
RetrievalResult
    ↓
Prompt Builder
    ↓
LLM
"""

from pydantic import BaseModel, ConfigDict


class RetrievalResult(BaseModel):
    """
    Represents a single search result returned by the retrieval engine.

    Attributes
    ----------
    chunk_id
        Identifier of the retrieved chunk.

    document_id
        Identifier of the source document.

    page_number
        Original page number.

    content
        Retrieved chunk text.

    similarity_score
        Similarity score assigned by the vector database.

    metadata
        Additional retrieval metadata.
    """

    chunk_id: str

    document_id: str

    page_number: int

    content: str

    similarity_score: float

    metadata: dict[str, str] = {}

    model_config = ConfigDict(
        extra="forbid"
    )