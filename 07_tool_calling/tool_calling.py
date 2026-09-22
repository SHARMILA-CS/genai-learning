import requests


# Tool function
def add_numbers(a, b):
    return a + b


# User question
question = input("Ask a calculation question: ")


# Define the available tool
tools = [
    {
        "type": "function",
        "function": {
            "name": "add_numbers",
            "description": "Add two numbers together.",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {
                        "type": "number",
                        "description": "First number"
                    },
                    "b": {
                        "type": "number",
                        "description": "Second number"
                    }
                },
                "required": ["a", "b"]
            }
        }
    }
]


# Send the question and tool definition to the LLM
url = "http://localhost:11434/api/chat"

data = {
    "model": "functiongemma",
    "messages": [
        {
            "role": "user",
            "content": question
        }
    ],
    "tools": tools,
    "stream": False
}


response = requests.post(
    url,
    json=data,
    timeout=120
)

response.raise_for_status()

result = response.json()

message = result["message"]


# Check whether the LLM requested a tool
if "tool_calls" in message:

    tool_call = message["tool_calls"][0]

    function_name = tool_call["function"]["name"]
    arguments = tool_call["function"]["arguments"]

    print("\nTool requested:", function_name)
    print("Arguments:", arguments)


    # Execute the requested tool
    if function_name == "add_numbers":

        tool_result = add_numbers(
            arguments["a"],
            arguments["b"]
        )

        print("\nTool result:", tool_result)

else:

    print("\nLLM response:")
    print(message["content"])