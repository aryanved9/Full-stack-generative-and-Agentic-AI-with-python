# Chain of Thought Prompting
import os
from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()

client = OpenAI(
    api_key= os.getenv("API_KEY"),
    base_url=os.getenv("BASE_URL")
)

SYSTEM_PROMPT= """
    you're an expert AI Assistant in resolving user queries using chain of thought.
    you work on START, PLAN and OUTPUT steps.
    you need to first PLAN what needs to be done. The PLAN can be multiple steps.
    Once you think enough PLAN has been done, finally you give an OUTPUT.
    
    Rules:
    - Strictly follow the given JSON output format 
    - Only run one step at a time.
    - The sequence of steps is START(where user gives an Input), PLAN (That can be multiple times) and finally OUTPUT (which is going to the displayed to the user).
    
    Output JSON Format:
    {"step": "START" | "PLAN" | "OUTPUT", "content": "string" }
    
   Examples:
   User: Hey, can you solve 2 + 3 * 20 / 5
   {"step": "START", "content": "User wants me to solve 2 + 3 * 20 / 5"}
   {"step": "PLAN", "content": "I should apply BODMAS here"}
   {"step": "PLAN", "content": "First, divide: 20 / 5 = 4"}
   {"step": "PLAN", "content": "Now the expression is 2 + 3 * 4"}
   {"step": "PLAN", "content": "Multiply: 3 * 4 = 12"}
   {"step": "PLAN", "content": "Add: 2 + 12 = 14"}
   {"step": "OUTPUT", "content": "14"}
"""

message_history = [
    {"role":"system", "content": SYSTEM_PROMPT},
]

user_query = input("👉 ")
message_history.append({"role": "user", "content": user_query})

while True:
    response = client.chat.completions.create(
        model='gemini-3.5-flash-lite',
        response_format={"type": "json_object"},
        messages= message_history
    )
    
    raw_result = response.choices[0].message.content
    message_history.append({"role": "assistant", "content": raw_result})
    
    try:
        parsed_result = json.loads(raw_result)
    except json.JSONDecodeError:
        print("⚠️ Invalid JSON from model:", raw_result)
        break
    
    step = parsed_result.get("step")
    content = parsed_result.get("content")
    
    if step == "OUTPUT":
        print("🔥", content)
        break
    
    if step == "START":
        print("🤓", content)
    elif step == "PLAN":
        print("🧠", content)
    else:
        print("⚠️ Unknown step:", parsed_result)
        break
        
    message_history.append({
        "role": "user",
        "content": "Continue with the next step ⚙️"
    })