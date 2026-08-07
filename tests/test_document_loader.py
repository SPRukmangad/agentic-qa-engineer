"""
Integration test for the document ingestion pipeline.

This test verifies that:

PDF
    ↓
DocumentLoader
    ↓
PDFLoader
    ↓
Document

works successfully.
"""

from pathlib import Path

from agentic_qa_engineer.ingestion import DocumentLoader


def main() -> None:
    """
    Test the PDF ingestion pipeline.
    """

    loader = DocumentLoader()

    document = loader.load(
        Path("data/attention.pdf")
    )

    print("=" * 60)
    print("Document successfully loaded")
    print("=" * 60)

    print(f"Document ID : {document.document_id}")
    print(f"File Name   : {document.file_name}")
    print(f"File Path   : {document.file_path}")
    print(f"Pages       : {document.page_count}")

    print("\nMetadata")
    print("-" * 60)
    print(document.metadata)

    print("\nContent Preview")
    print("-" * 60)
    print(document.content[:500])


if __name__ == "__main__":
    main()