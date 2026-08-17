"""
Configuration for the vector store pipeline.

This module contains configuration required to initialize
and connect to the vector store.
"""

from enum import Enum

from pydantic import BaseModel, Field


class DistanceMetric(str, Enum):
    """
    Supported distance metrics for vector similarity search.
    """

    COSINE = "cosine"
    DOT = "dot"
    EUCLID = "euclid"


class VectorStoreConfig(BaseModel):
    """
    Configuration for an vector store.

    Attributes
    ----------
    collection_name
        Name of the vector collection.

    host
        Host address of the vector database.

    port
        Port used by vector database.

    distance
        Distance metric used for vector similarity search.

    """

    collection_name: str = Field(
        default="agentic-qa-engineer",
        description="Name of the vector collection.",
    )

    host: str = Field(
        default="localhost",
        description="Host address of the Qdrant server.",
    )

    port: int = Field(
        default=6333,
        gt=0,
        description="Port used by the Qdrant server.",
    )

    distance: DistanceMetric = Field(
        default =DistanceMetric.COSINE,
        description="Distance metric used for vector similarity search.",
    )