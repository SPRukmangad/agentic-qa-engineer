"""
recursive_chunker.py

Recursive document chunking implementation.

Purpose
-------
This module implements the Recursive Character Text Splitting strategy
using LangChain's RecursiveCharacterTextSplitter.

Why Recursive Chunking?
-----------------------
Recursive chunking is a production-proven baseline strategy that
attempts to preserve semantic boundaries while respecting chunk size
constraints.

Instead of splitting text at a fixed number of characters, it tries
multiple separators in order:

Paragraph
    ↓
Sentence
    ↓
Word
    ↓
Character

Benefits
--------
- Preserves semantic meaning
- Produces consistent chunk sizes
- Works well across different document types
- Excellent baseline for Retrieval-Augmented Generation (RAG)

Future Improvements
-------------------
Alternative chunking strategies can be introduced by implementing the
BaseChunker interface without changing downstream components.
"""

from uuid import uuid4

from langchain_text_splitters import RecursiveCharacterTextSplitter

from agentic_qa_engineer.chunking.base_chunker import BaseChunker
from agentic_qa_engineer.chunking.chunking_config import ChunkingConfig
from agentic_qa_engineer.models import Document, DocumentChunk


class RecursiveChunker(BaseChunker):
    """
    Recursive implementation of the BaseChunker interface.

    This chunker delegates the splitting algorithm to LangChain's
    RecursiveCharacterTextSplitter while converting the output into
    the application's DocumentChunk domain model.
    """

    def __init__(self, config: ChunkingConfig) -> None:
        """
        Initialize the recursive chunker.

        Parameters
        ----------
        config
            Chunking configuration.
        """

        self._config = config

        self._text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=config.chunk_size,
            chunk_overlap=config.chunk_overlap,
            separators=config.separators,
            keep_separator=config.keep_separator,
        )

    def chunk(self, document: Document) -> list[DocumentChunk]:
        """
        Split a document into chunks.

        Parameters
        ----------
        document
            Source document.

        Returns
        -------
        list[DocumentChunk]
            List of generated chunks.
        """

        chunks = self._text_splitter.split_text(
            document.content
        )

        document_chunks: list[DocumentChunk] = []

        for index, chunk in enumerate(chunks):

            document_chunks.append(
                DocumentChunk(
                    chunk_id=str(uuid4()),
                    document_id=document.document_id,
                    chunk_index=index,
                    page_number=0,
                    content=chunk,
                    metadata=document.metadata,
                )
            )

        return document_chunks