"""
Configuration for the embedding pipeline.

This module contains configuration required to initialize
and use an embedding model.
"""

from pydantic import BaseModel, Field


class EmbeddingConfig(BaseModel):
    """
    Configuration for an embedding model.

    Attributes
    ----------
    model_name
        Name of the embedding model to use.

    device
        Device on which the model should run.
        Examples: "cpu", "cuda".

    batch_size
        Number of texts processed together during embedding.

    normalize_embeddings
        Whether generated embeddings should be normalized.

    cache_dir
        Optional directory used to cache the downloaded model.
    """

    model_name: str = Field(
        default="BAAI/bge-small-en-v1.5",
        description="Name of the embedding model.",
    )

    device: str = Field(
        default="cpu",
        description="Device used for embedding generation.",
    )

    batch_size: int = Field(
        default=32,
        gt=0,
        description="Number of texts processed in one batch.",
    )

    normalize_embeddings: bool = Field(
        default=True,
        description="Whether to normalize generated embeddings.",
    )

    cache_dir: str | None = Field(
        default=None,
        description="Optional directory for model caching.",
    )