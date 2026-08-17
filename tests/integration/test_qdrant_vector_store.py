from agentic_qa_engineer.vector_store import (
    QdrantVectorStore,
    VectorStoreConfig,
)


def test_qdrant_vector_store_initializes():
    config = VectorStoreConfig(
        collection_name="test-agentic-qa",
    )

    store = QdrantVectorStore(
        config=config,
        vector_size=384,
    )

    assert store._client.collection_exists(config.collection_name)


import uuid

from agentic_qa_engineer.embeddings import EmbeddingResult
from agentic_qa_engineer.models import DocumentChunk


def test_qdrant_vector_store_adds_embeddings():
    config = VectorStoreConfig(
        collection_name="test-agentic-qa-add",
    )

    store = QdrantVectorStore(
        config=config,
        vector_size=3,
    )

    chunk_1_id = str(uuid.uuid4())
    chunk_2_id = str(uuid.uuid4())

    chunks = [
        DocumentChunk(
            chunk_id=chunk_1_id,
            document_id="doc-1",
            chunk_index=0,
            page_number=1,
            content="Python is a programming language.",
            metadata={"source": "test"},
        ),
        DocumentChunk(
            chunk_id=chunk_2_id,
            document_id="doc-1",
            chunk_index=1,
            page_number=1,
            content="Qdrant is a vector database.",
            metadata={"source": "test"},
        ),
    ]

    embeddings = [
        EmbeddingResult(
            chunk_id=chunk_1_id,
            vector=[1.0, 0.0, 0.0],
            model_name="test-model",
            dimensions=3,
        ),
        EmbeddingResult(
            chunk_id=chunk_2_id,
            vector=[0.0, 1.0, 0.0],
            model_name="test-model",
            dimensions=3,
        ),
    ]

    store.add(
        chunks=chunks,
        embeddings=embeddings,
    )

    points = store._client.retrieve(
        collection_name=config.collection_name,
        ids=[chunk_1_id, chunk_2_id],
    )

    assert len(points) == 2
    assert points[0].payload["content"] == ("Python is a programming language.")
    assert points[1].payload["content"] == ("Qdrant is a vector database.")


def test_qdrant_vector_store_searches_embeddings():
    config = VectorStoreConfig(
        collection_name="test-agentic-qa-search",
    )

    store = QdrantVectorStore(
        config=config,
        vector_size=3,
    )

    chunk_1_id = str(uuid.uuid4())
    chunk_2_id = str(uuid.uuid4())

    chunks = [
        DocumentChunk(
            chunk_id=chunk_1_id,
            document_id="doc-1",
            chunk_index=0,
            page_number=1,
            content="Python is a programming language.",
            metadata={"source": "test"},
        ),
        DocumentChunk(
            chunk_id=chunk_2_id,
            document_id="doc-1",
            chunk_index=1,
            page_number=1,
            content="Qdrant is a vector database.",
            metadata={"source": "test"},
        ),
    ]

    embeddings = [
        EmbeddingResult(
            chunk_id=chunk_1_id,
            vector=[1.0, 0.0, 0.0],
            model_name="test-model",
            dimensions=3,
        ),
        EmbeddingResult(
            chunk_id=chunk_2_id,
            vector=[0.0, 1.0, 0.0],
            model_name="test-model",
            dimensions=3,
        ),
    ]

    store.add(
        chunks=chunks,
        embeddings=embeddings,
    )

    results = store.search(
        query_vector=[1.0, 0.0, 0.0],
        top_k=2,
    )

    assert len(results) == 2

    assert results[0].chunk.chunk_id == chunk_1_id
    assert results[0].chunk.content == ("Python is a programming language.")

    assert results[0].score > results[1].score
