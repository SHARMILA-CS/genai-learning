import requests
import json

question = input("Enter a person description: ")

url = "http://localhost:11434/api/generate"

prompt = f"""
Extract information from the following text.

Return ONLY valid JSON in this exact format:

{{
    "name": "string",
    "age": 0,
    "skills": []
}}

Text:
{question}
"""

data = {
    "model": "gemma3:4b",
    "prompt": prompt,
    "stream": False,
    "format": "json",
    "options": {
        "temperature": 0.2,
        "num_predict": 200
    }
}

response = requests.post(url, json=data)

result = response.json()

json_data = json.loads(result["response"])

print("\nStructured data:")
print(json_data)

print("\nName:", json_data["name"])
print("Age:", json_data["age"])
print("Skills:", json_data["skills"])