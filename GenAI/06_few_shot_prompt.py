import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key= os.getenv("API_KEY"),
    base_url=os.getenv("BASE_URL")
)

# zero shot prompting: The model is given a direct instructions and few examples.

SYSTEM_PROMPT = """ 
you should only and only answer coding related questions, Do not answer anything else. your name is Alexa, if user asks anything other than coding just say sorry i can only resolve coding problems.

Rule: Strictly follow the output in JSON Format
OUTPUT FORMAT:
{{
    "code":"string" or None,
    "isCodingQuestion": bool
}}

Examples:
Q: can you explain the a + b whole Square?
A: {{"code": None, "isCodingQuestion": False}}

Q: Hey, write a code in python for adding two numbers
A: {{"code": "def add(a,b):
        return a + b", "isCodingQuestion": True}}

"""

response = client.chat.completions.create(
    model='gemini-3.5-flash-lite',
    messages=[
        {"role":"system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Hi, can you help me to write find factorial in Python"}
    ]
)

print(response.choices[0].message.content)