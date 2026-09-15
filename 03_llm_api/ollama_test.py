import requests
question = input("Enter your question: ")
url = "http://localhost:11434/api/generate"
data = {
    "model": "gemma3:4b",
    "prompt": question,
    "stream": False,
    "options": {
        "num_predict": 200,
        "temperature": 0.2
    }
}
try:
    response = requests.post(url, json=data, timeout=60)
    response.raise_for_status()
    result = response.json()
    print("\nGemma:", result["response"])
except requests.exceptions.ConnectionError:
    print("\nError: Could not connect to Ollama. Make sure Ollama is running.")
except requests.exceptions.Timeout:
    print("\nError: The request took too long.")
except requests.exceptions.RequestException as e:
    print("\nRequest error:", e)
