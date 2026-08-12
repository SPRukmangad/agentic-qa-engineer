from pathlib import Path

from agentic_qa_engineer.chunking import (
    ChunkingConfig,
    RecursiveChunker,
)
from agentic_qa_engineer.embeddings import (
    EmbeddingConfig,
    SentenceTransformerEmbedder,
)
from agentic_qa_engineer.ingestion import DocumentLoader


def main() -> None:
    """Test the document-to-embedding pipeline."""

    # 1. Load the document
    loader = DocumentLoader()

    document = loader.load(
        Path("data/attention.pdf")
    )

    # 2. Chunk the document
    chunker = RecursiveChunker(
        ChunkingConfig(
            chunk_size=1000,
            chunk_overlap=200,
        )
    )

    chunks = chunker.chunk(document)

    print(f"Total chunks: {len(chunks)}")

    # 3. Embed the chunks
    embedder = SentenceTransformerEmbedder(
        EmbeddingConfig(
            model_name="BAAI/bge-small-en-v1.5",
            device="cpu",
            batch_size=32,
            normalize_embeddings=True,
        )
    )

    embeddings = embedder.embed(chunks)

    print(f"Total embeddings: {len(embeddings)}")
    print(f"Model: {embeddings[0].model_name}")
    print(f"Dimensions: {embeddings[0].dimensions}")
    print(f"First vector length: {len(embeddings[0].vector)}")
    print(f"First chunk ID: {embeddings[0].chunk_id}")


if __name__ == "__main__":
    main()