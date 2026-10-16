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
        {"role": "user", "content": "Explain to me how AI works"}
    ]
)

print(response.choices[0].message.content)