# Chain of Thought Prompting
import os
from dotenv import load_dotenv
from openai import OpenAI
import json
import requests

load_dotenv()

client = OpenAI(
    api_key= os.getenv("API_KEY"),
    base_url=os.getenv("BASE_URL")
)

def get_weather(city: str):
    url = f"https://wttr.in/{city.lower()}?format=%c+%t"
    respose = requests.get(url)
    
    if respose.status_code == 200:
        return f"The weather in {city} is {respose.text}"
    
    raise ValueError("failed to fetch")

available_tool = {
    "get_weather": get_weather
}

SYSTEM_PROMPT= """
    you're an expert AI Assistant in resolving user queries using chain of thought.
    you work on START, PLAN and OUTPUT steps.
    you need to first PLAN what needs to be done. The PLAN can be multiple steps.
    Once you think enough PLAN has been done, finally you give an OUTPUT.
    you can also call a tool if required from the list of avaiable tools.
    for every tool call wait for the observe step which is the output from the called tool.
    Go Through OUTPUT step in end of things to exit correctly
    
    Rules:
    - Strictly follow the given JSON output format 
    - Only run one step at a time.
    - The sequence of steps is START(where user gives an Input), PLAN (That can be multiple times) and finally OUTPUT (which is going to the displayed to the user).
    
    Output JSON Format:
    {"step": "START" | "PLAN" | "OUTPUT" | "TOOL", "content": "string", "tool": "string", "input": "string" }
    
    Available Tools:
    -get_weather(city: str): Takes city name as input string and return weather information about the city
    
    Examples 1:
    User: Hey, can you solve 2 + 3 * 20 / 5
    {"step": "START", "content": "User wants me to solve 2 + 3 * 20 / 5"}
    {"step": "PLAN", "content": "I should apply BODMAS here"}
    {"step": "PLAN", "content": "First, divide: 20 / 5 = 4"}
    {"step": "PLAN", "content": "Now the expression is 2 + 3 * 4"}
    {"step": "PLAN", "content": "Multiply: 3 * 4 = 12"}
    {"step": "PLAN", "content": "Add: 2 + 12 = 14"}
    {"step": "OUTPUT", "content": "14"}
    
    Examples 2:
    User: what is the weather of delhi?
    {"step": "START", "content": "seems like user is interested in getting weather of delhi in India"}
    {"step": "PLAN", "content": "Lets see if we have any available tool from the list of available tools"}
    {"step": "PLAN", "content": "Great ! we have get_weather tool available for this query"}
    {"step": "PLAN", "content": "I need to call get_weather tool for delhi as input for city"}
    {"step": "TOOL", "tool": "get_weather", "input": "delhi"}
    {"step": "OBSERVE", "tool": "get_weather", "output": "the temp of delhi is cloudy with 20 C"}
    {"step": "OUTPUT", "content": "The current weather in delhi is 20 C with cloudy sky."}
"""

message_history = [
    {"role":"system", "content": SYSTEM_PROMPT},
]
while True:
    user_query = input("👉 ")
    message_history.append({"role": "user", "content": user_query})

    while True:
        try:
            response = client.chat.completions.create(
            model='gemini-3.5-flash-lite',
            response_format={"type": "json_object"},
            messages= message_history
        )
        except Exception as e:
            print("⚠️ API error:", e)
            break
        
        raw_result = response.choices[0].message.content
        message_history.append({"role": "assistant", "content": raw_result})
        
        try:
            parsed_result = json.loads(raw_result)
        except json.JSONDecodeError:
            print("⚠️ Invalid JSON from model:", raw_result)
            break
        
        step = parsed_result.get("step")
        content = parsed_result.get("content")
            
        if step == "START":
            print("🤓", content)
        elif step == "PLAN":
            print("🧠", content)
        elif step == "TOOL":
            tool_to_call = parsed_result.get("tool")
            tool_input = parsed_result.get("input")
            print(f"⚒️: {tool_to_call}({tool_input})")
            tool_response = available_tool[tool_to_call](tool_input)
            print(f"⚒️: {tool_to_call}({tool_input}) = {tool_response}")
            message_history.append({"role":"user", "content": json.dumps(
                {"step":"OBSERVE", "tool": tool_to_call, "output": tool_response }
            )})
            continue
        elif step == "OUTPUT":
            print("🔥", content)
            break
            
        message_history.append({
            "role": "user",
            "content": "Continue with the next step ⚙️"
        })