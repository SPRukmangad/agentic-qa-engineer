"""
search_result.py

Domain model representing a vector search result.
"""

from pydantic import BaseModel, Field

from agentic_qa_engineer.models import DocumentChunk


class SearchResult(BaseModel):
    """
    Represents a single result returned by vector similarity search.

    Attributes
    ----------
    chunk
        Document chunk retrieved from the vector store.

    score
        Similarity score between the query vector and the stored vector.
    """

    chunk: DocumentChunk = Field(
        description="Document chunk retrieved from the vector store.",
    )

    score: float = Field(
        description="Similarity score for the retrieved chunk.",
    )