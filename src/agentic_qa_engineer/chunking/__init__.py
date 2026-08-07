"""
Document chunking package.

This package contains all chunking strategies used by the
Agentic QA Engineer.

Responsibilities
----------------
- Split documents into smaller chunks
- Provide interchangeable chunking strategies
- Produce DocumentChunk domain objects

Current Strategy
----------------
- Recursive Character Chunking

Future Strategies
-----------------
- Semantic Chunking
- Markdown-aware Chunking
- Parent-Child Chunking

Public API
----------
The rest of the application should import chunkers only from this
package instead of importing individual implementation modules.

Example
-------

from agentic_qa_engineer.chunking import (
    RecursiveChunker,
    ChunkingConfig,
)
"""

from .base_chunker import BaseChunker
from .chunking_config import ChunkingConfig
from .recursive_chunker import RecursiveChunker

__all__ = [
    "BaseChunker",
    "ChunkingConfig",
    "RecursiveChunker",
]