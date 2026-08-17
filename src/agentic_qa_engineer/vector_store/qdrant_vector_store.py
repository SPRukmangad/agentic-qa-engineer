"""
qdrant_vector_store.py

Qdrant implementation of the BaseVectorStore interface.
"""

from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    PointStruct,
    VectorParams,
)

from agentic_qa_engineer.embeddings import EmbeddingResult
from agentic_qa_engineer.models import DocumentChunk
from agentic_qa_engineer.vector_store.base_vector_store import BaseVectorStore
from agentic_qa_engineer.vector_store.search_result import SearchResult
from agentic_qa_engineer.vector_store.vector_store_config import (
    DistanceMetric,
    VectorStoreConfig,
)


class QdrantVectorStore(BaseVectorStore):
    """
    Qdrant implementation of the vector store.

    Stores embedding vectors together with the metadata required
    to reconstruct the original DocumentChunk.
    """

    def __init__(
        self,
        config: VectorStoreConfig,
        vector_size: int,
    ) -> None:
        """
        Initialize the Qdrant vector store.

        Parameters
        ----------
        config
            Qdrant connection and collection configuration.

        vector_size
            Dimensionality of the embedding vectors.
        """

        self._config = config
        self._vector_size = vector_size

        self._client = QdrantClient(
            host=config.host,
            port=config.port,
        )

        self._ensure_collection()

    def _ensure_collection(self) -> None:
        """Create the collection if it does not already exist."""

        if self._client.collection_exists(
            self._config.collection_name
        ):
            return

        self._client.create_collection(
            collection_name=self._config.collection_name,
            vectors_config=VectorParams(
                size=self._vector_size,
                distance=self._get_qdrant_distance(),
            ),
        )

    def _get_qdrant_distance(self) -> Distance:
        """Convert our domain enum to Qdrant's distance enum."""

        distance_mapping = {
            DistanceMetric.COSINE: Distance.COSINE,
            DistanceMetric.DOT: Distance.DOT,
            DistanceMetric.EUCLID: Distance.EUCLID,
        }

        return distance_mapping[self._config.distance]

    def add(
        self,
        chunks: list[DocumentChunk],
        embeddings: list[EmbeddingResult],
    ) -> None:
        """
        Add document chunks and their embeddings to Qdrant.

        Each chunk and its corresponding embedding are stored
        together as one Qdrant point.
        """

        if not chunks:
            return

        if len(chunks) != len(embeddings):
            raise ValueError(
                "Number of chunks must match number of embeddings."
            )

        points = []

        for chunk, embedding in zip(chunks, embeddings):
            if chunk.chunk_id != embedding.chunk_id:
                raise ValueError(
                    f"Chunk ID {chunk.chunk_id} does not match "
                    f"embedding ID {embedding.chunk_id}."
                )

            points.append(
                PointStruct(
                    id=chunk.chunk_id,
                    vector=embedding.vector,
                    payload={
                        "chunk_id": chunk.chunk_id,
                        "document_id": chunk.document_id,
                        "chunk_index": chunk.chunk_index,
                        "page_number": chunk.page_number,
                        "content": chunk.content,
                        "metadata": chunk.metadata,
                    },
                )
            )

        self._client.upsert(
            collection_name=self._config.collection_name,
            points=points,
        )

    def search(
        self,
        query_vector: list[float],
        top_k: int = 5,
    ) -> list[SearchResult]:
        """
        Search Qdrant for the most similar vectors.
        """

        results = self._client.query_points(
            collection_name=self._config.collection_name,
            query=query_vector,
            limit=top_k,
        ).points

        search_results = []

        for result in results:
            payload = result.payload or {}

            chunk = DocumentChunk(
                chunk_id=payload["chunk_id"],
                document_id=payload["document_id"],
                chunk_index=payload["chunk_index"],
                page_number=payload["page_number"],
                content=payload["content"],
                metadata=payload.get("metadata", {}),
            )

            search_results.append(
                SearchResult(
                    chunk=chunk,
                    score=result.score,
                )
            )

        return search_results