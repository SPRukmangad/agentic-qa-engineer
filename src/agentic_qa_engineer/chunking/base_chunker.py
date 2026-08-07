"""
base_chunker.py

Abstract base class for all document chunking strategies.

Purpose
-------
This module defines the contract that every chunking strategy must
implement.

Why do we need this?
--------------------
The Agentic QA Engineer may support multiple chunking strategies:

- Recursive Character Chunking
- Semantic Chunking
- Markdown-aware Chunking
- Parent-Child Chunking

Instead of tightly coupling the application to one implementation,
all chunkers implement the same interface.

Benefits
--------
- Extensible architecture
- Easy experimentation
- Strategy interchangeability
- Supports Open/Closed Principle

The rest of the application only interacts with BaseChunker and
does not need to know which concrete implementation is being used.
"""

from abc import ABC, abstractmethod

from agentic_qa_engineer.models import Document, DocumentChunk


class BaseChunker(ABC):
    """
    Abstract base class for all chunking strategies.

    Every chunker must implement the `chunk()` method.

    This ensures a consistent interface across different chunking
    implementations.
    """

    @abstractmethod
    def chunk(self, document: Document) -> list[DocumentChunk]:
        """
        Split a document into smaller chunks.

        Parameters
        ----------
        document : Document
            Source document to be chunked.

        Returns
        -------
        list[DocumentChunk]
            List of generated document chunks.
        """

        raise NotImplementedError