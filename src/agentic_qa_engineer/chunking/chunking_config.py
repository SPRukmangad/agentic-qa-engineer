"""
chunking_config.py

Configuration for document chunking.

Purpose
-------
This module centralizes all chunking-related configuration used by the
chunking pipeline.

Why do we need this?
--------------------
Chunking parameters such as chunk size and overlap significantly impact
retrieval quality.

Keeping these values separate from the implementation allows us to
experiment with different strategies without modifying the chunking
logic.

Examples
--------
Instead of changing:

    RecursiveChunker(chunk_size=500)

inside the implementation every time, we simply update the
configuration in one place.

Future Improvements
-------------------
As additional chunking strategies are introduced (Semantic Chunking,
Markdown Chunking, Parent-Child Chunking), this configuration can be
extended while keeping the implementation unchanged.
"""

from pydantic import BaseModel, Field


class ChunkingConfig(BaseModel):
    """
    Configuration for recursive document chunking.

    Attributes
    ----------
    chunk_size
        Maximum size of each chunk in characters.

    chunk_overlap
        Number of overlapping characters between consecutive chunks.

    separators
        Ordered list of separators used by the recursive splitter.

    keep_separator
        Whether separators should be retained in the resulting chunks.
    """

    chunk_size: int = Field(
        default=1000,
        gt=0,
        description="Maximum number of characters per chunk.",
    )

    chunk_overlap: int = Field(
        default=200,
        ge=0,
        description="Number of overlapping characters between chunks.",
    )

    separators: list[str] = Field(
        default_factory=lambda: [
            "\n\n",
            "\n",
            ". ",
            " ",
            "",
        ],
        description="Ordered separators used during recursive splitting.",
    )

    keep_separator: bool = Field(
        default=True,
        description="Whether to preserve separators during chunking.",
    )