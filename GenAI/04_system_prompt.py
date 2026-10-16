import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key= os.getenv("API_KEY"),
    base_url=os.getenv("BASE_URL")
)

response = client.chat.completions.create(
    model='gemini-3.5-flash-lite',
    messages=[
        {"role":"system", "content":"You are expert in Maths, and only and only answer Maths related problem. If query is not related to Maths do Not answer."},
        {"role": "user", "content": "Hi, can you help me solve the a + b whole square in short words"}
    ]
)

print(response.choices[0].message.content)