import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key= os.getenv("API_KEY"),
    base_url=os.getenv("BASE_URL")
)

# zero shot prompting: The model is given a direct question or task without any prior examples.

SYSTEM_PROMPT = "you should only and only answer coding related questions, Do not answer anything else. your name is Alexa, if user asks anything other than coding just say sorry i can only resolve coding problems"

response = client.chat.completions.create(
    model='gemini-3.5-flash-lite',
    messages=[
        {"role":"system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Hi, how to Play Football"}
    ]
)

print(response.choices[0].message.content)