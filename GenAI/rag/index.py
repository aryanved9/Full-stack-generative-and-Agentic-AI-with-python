from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

pdf_path = Path(__file__).parent / "Aryan_ved_RESUME_.PDF"

# Load this file in python program

loader = PyPDFLoader(file_path=pdf_path)
docs = loader.load()
print(docs[0])

#  split the docs(pages) into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=150,
    chunk_overlap=100
)

chunks = text_splitter.split_documents(documents=docs)
print("___________________________________ CHUNKS OUTPUT")
print(chunks)