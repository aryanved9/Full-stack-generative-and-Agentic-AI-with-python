import os   
from dotenv import load_dotenv
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore

load_dotenv()

pdf_path = Path(__file__).parent / "Aryan_ved_RESUME_.PDF"

# Load this file in python program

loader = PyPDFLoader(file_path=pdf_path)
docs = loader.load()
# print(docs[0])

#  split the docs(pages) into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=150,
    chunk_overlap=100
)

chunks = text_splitter.split_documents(documents=docs)
# print("___________________________________ CHUNKS OUTPUT")
# print(chunks)

# vector embedding for chunks
embedding_model = OpenAIEmbeddings(
    model="gemini-embedding-2-preview",
    api_key=os.getenv("API_KEY"),
    base_url=os.getenv("BASE_URL"),
    check_embedding_ctx_length=False,
    encoding_format="float"
)

vector_store = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="learning_rag"
)

print("Indexing of document done...")