import os   
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key= os.getenv("API_KEY"),
    base_url=os.getenv("BASE_URL")
)

embedding_model = OpenAIEmbeddings(
    model="gemini-embedding-2-preview",
    api_key=os.getenv("API_KEY"),
    base_url=os.getenv("BASE_URL"),
    check_embedding_ctx_length=False,
    encoding_format="float"
)

vector_db = QdrantVectorStore.from_existing_collection(
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="learning_rag"
)

# Take user input
user_query= input(f"👉Ask something: ")

# Relevant chunks from the vector db
search_results = vector_db.similarity_search(query=user_query)

context = "\n\n\n".join([f"page content: {result.page_content}\n Page Number: {result.metadata['page_label']}\nFile Location: {result.metadata['source']}" for result in search_results])

SYSTEM_PROMPT= f""""
 you are a helpfull AI Assistant who answers user query based on the available context retrieved from a pdf file along with page_content.
 you should only ans the user based on the following context and navigate the user to see and know more.
 
 context: {context}
"""

response = client.chat.completions.create(
    model='gemini-3.5-flash-lite',
    messages=[
        {"role":"system", "content":SYSTEM_PROMPT},
        {"role": "user", "content": user_query}
    ]
)

print(f"🤖: {response.choices[0].message.content}")