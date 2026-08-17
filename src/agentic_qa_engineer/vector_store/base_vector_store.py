"""
base_vector_store.py

Abstract interface for vector store implementations.
"""

from abc import ABC, abstractmethod

from agentic_qa_engineer.embeddings import EmbeddingResult
from agentic_qa_engineer.models import DocumentChunk
from agentic_qa_engineer.vector_store.search_result import SearchResult


class BaseVectorStore(ABC):
    """
    Abstract base class for all vector store implementations.
    """

    @abstractmethod
    def add(
        self,
        chunks: list[DocumentChunk],
        embeddings: list[EmbeddingResult],
    ) -> None:
        """
        Add document chunks and their embeddings to the vector store.

        Parameters
        ----------
        chunks
            Original document chunks.

        embeddings
            Embeddings corresponding to the document chunks.
        """

        raise NotImplementedError

    @abstractmethod
    def search(
        self,
        query_vector: list[float],
        top_k: int = 5,
    ) -> list[SearchResult]:
        """
        Search for vectors similar to the query vector.

        Parameters
        ----------
        query_vector
            Embedding vector representing the user query.

        top_k
            Maximum number of results to return.

        Returns
        -------
        list[SearchResult]
            Most relevant chunks and their similarity scores.
        """

        raise NotImplementedError
