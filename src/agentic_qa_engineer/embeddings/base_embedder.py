"""
base_embedder.py

Abstract interface for embedding implementations.

This module defines the contract that every embedding provider
must follow.
"""

from abc import ABC, abstractmethod

from agentic_qa_engineer.models import DocumentChunk
from agentic_qa_engineer.embeddings.embedding_result import EmbeddingResult


class BaseEmbedder(ABC):
    """
    Abstract base class for all embedding implementations.

    Concrete implementations must convert DocumentChunk objects
    into embedding vectors.
    """

    @abstractmethod
    def embed(
        self,
        chunks: list[DocumentChunk],
    ) -> list[EmbeddingResult]:
        """
        Generate embeddings for document chunks.

        Parameters
        ----------
        chunks
            Document chunks that need to be embedded.

        Returns
        -------
        list[EmbeddingResult]
            Generated embeddings corresponding to the input chunks.
        """

        raise NotImplementedError