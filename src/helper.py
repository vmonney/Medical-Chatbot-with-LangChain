"""Helper functions for the main script."""
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings


# Extract data from the PDF
def load_pdf(data: str) -> list:
    """Load PDF files from a directory and return a list of Document objects."""
    loader = DirectoryLoader(data, glob="*.pdf", loader_cls=PyPDFLoader)

    return loader.load()


# Create text chunks
def text_split(extracted_data: list) -> list:
    """Split the text into chunks of 500 characters with an overlap of 20 characters."""
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
    return text_splitter.split_documents(extracted_data)


# download embedding model
def download_hugging_face_embeddings() -> HuggingFaceEmbeddings:
    """Download the HuggingFace embedding model."""
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
    )
