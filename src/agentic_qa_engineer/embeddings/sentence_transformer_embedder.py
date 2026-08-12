"""
sentence_transformer_embedder.py

Sentence Transformers implementation of the BaseEmbedder interface.
"""

from sentence_transformers import SentenceTransformer

from agentic_qa_engineer.embeddings.base_embedder import BaseEmbedder
from agentic_qa_engineer.embeddings.embedding_config import EmbeddingConfig
from agentic_qa_engineer.embeddings.embedding_result import EmbeddingResult
from agentic_qa_engineer.models import DocumentChunk


class SentenceTransformerEmbedder(BaseEmbedder):
    """
    Generate embeddings using a Sentence Transformers model.
    """

    def __init__(self, config: EmbeddingConfig) -> None:
        """
        Initialize the embedding model.

        Parameters
        ----------
        config
            Configuration for the embedding model.
        """

        self._config = config

        self._model = SentenceTransformer(
            config.model_name,
            device=config.device,
            cache_folder=config.cache_dir,
        )

    def embed(
        self,
        chunks: list[DocumentChunk],
    ) -> list[EmbeddingResult]:
        """
        Generate embeddings for document chunks.

        Parameters
        ----------
        chunks
            Document chunks to embed.

        Returns
        -------
        list[EmbeddingResult]
            Embeddings corresponding to the input chunks.
        """

        if not chunks:
            return []

        texts = [chunk.content for chunk in chunks]

        vectors = self._model.encode(
            texts,
            batch_size=self._config.batch_size,
            normalize_embeddings=self._config.normalize_embeddings,
            convert_to_numpy=True,
        )

        return [
            EmbeddingResult(
                chunk_id=chunk.chunk_id,
                vector=vector.tolist(),
                model_name=self._config.model_name,
                dimensions=len(vector),
            )
            for chunk, vector in zip(chunks, vectors)
        ]