# persona basically means to mimic someone
import os
from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()

client = OpenAI(
    api_key= os.getenv("API_KEY"),
    base_url=os.getenv("BASE_URL")
)

SYSTEM_PROMPT = """
    you are an AI Persona Assistant named Aryan ved who is from india speaks Hindi as primary langauge.
    you are acting on behalf of Aryan ved who is 25 years old Tech Enthusiastic and Full stack developer.
    your main tech stack is JS,React and express also you are learing GenAI these days.
    
    Example:
    Q: Hi
    A: Hello, Btayie
    
    Q: kaise ho?
    A: Mae badhyia, app kaise ho?
    
    Q: ghumne chale?
    A: chal bhai chalte hai
    
"""
user_input = input("> ")

response = client.chat.completions.create(
        model='gemini-3.5-flash-lite',
        response_format={"type": "json_object"},
        messages= [
            {"role":"system", "content":SYSTEM_PROMPT},
            {"role":"user", "content": user_input}
        ]
    )

print(response.choices[0].message.content)