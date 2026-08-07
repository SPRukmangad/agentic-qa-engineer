from pathlib import Path

from agentic_qa_engineer.chunking import (
    ChunkingConfig,
    RecursiveChunker,
)
from agentic_qa_engineer.ingestion import DocumentLoader


def main() -> None:

    loader = DocumentLoader()

    document = loader.load(
        Path("data/attention.pdf")
    )

    config = ChunkingConfig()

    chunker = RecursiveChunker(config)

    chunks = chunker.chunk(document)

    print("=" * 60)
    print(f"Document Name : {document.file_name}")
    print(f"Total Chunks  : {len(chunks)}")
    print("=" * 60)

    print("\nFirst Chunk\n")
    print(chunks[0].content[:500])


if __name__ == "__main__":
    main()