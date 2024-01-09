"""Store the embeddings of the text chunks in the pinecone index."""
import os

import pinecone
from dotenv import load_dotenv
from langchain_community.vectorstores import Pinecone

from src.helper import download_hugging_face_embeddings, load_pdf, text_split

load_dotenv()

PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
PINECONE_API_ENV = os.environ.get("PINECONE_API_ENV")

extracted_data = load_pdf("data/")
text_chunks = text_split(extracted_data)
embeddings = download_hugging_face_embeddings()

# Initializing the Pinecone
pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_API_ENV)

index_name = "medical-chatbot"

# Creating Embeddings for Each of The Text Chunks & storing
docsearch = Pinecone.from_texts(
    [t.page_content for t in text_chunks],
    embeddings,
    index_name=index_name,
)
