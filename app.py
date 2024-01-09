"""Main file for the chatbot."""

import os

import pinecone
from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers
from langchain_community.vectorstores import Pinecone

from src.helper import download_hugging_face_embeddings
from src.prompt import prompt_template

app = Flask(__name__)

load_dotenv()

PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
PINECONE_API_ENV = os.environ.get("PINECONE_API_ENV")

embeddings = download_hugging_face_embeddings()

# Initializing the Pinecone
pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_API_ENV)
index_name = "medical-chatbot"

# Load the index
docsearch = Pinecone.from_existing_index(index_name, embeddings)

PROMPT = PromptTemplate(
    template=prompt_template,
    input_variables=["context", "question"],
)
chain_type_kwargs = {"prompt": PROMPT}

llm = CTransformers(
    model="models/llama-2-7b-chat.ggmlv3.q4_0.bin",
    model_type="llama",
    config={"max_new_tokens": 1024, "temperature": 0.8},
)

qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=docsearch.as_retriever(search_kwargs={"k": 2}),
    return_source_documents=True,
    chain_type_kwargs=chain_type_kwargs,
)


@app.route("/")
def index() -> str:
    """Index page."""
    return render_template("chat.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
