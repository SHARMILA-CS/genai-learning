import os
from dotenv import load_dotenv
import requests
import chromadb
from sentence_transformers import SentenceTransformer


# Load environment variables
load_dotenv()

OLLAMA_URL = os.getenv("OLLAMA_URL")
MODEL_NAME = os.getenv("MODEL_NAME")


# 1. Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# 2. Connect to Chroma database
client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_collection(
    name="college_rules"
)


def answer_question(question):

    # 3. Convert question into an embedding
    question_embedding = model.encode(question).tolist()


    # 4. Retrieve relevant chunks
    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=2
    )

    retrieved_chunks = results["documents"][0]


    # 5. Combine retrieved chunks
    context = "\n\n".join(retrieved_chunks)


    # 6. Create prompt for Gemma
    prompt = f"""
Answer the question using only the information provided in the context.
If the answer is not present in the context, say:
"I don't know based on the provided information."

Context:
{context}

Question:
{question}

Answer:
"""


    # 7. Prepare Ollama request
    url = OLLAMA_URL

    data = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.2,
            "num_predict": 150
        }
    }


    # 8. Send request to Ollama with error handling
    try:

        response = requests.post(
            url,
            json=data,
            timeout=60
        )

        response.raise_for_status()

        result = response.json()

        return result["response"]


    except requests.exceptions.RequestException as e:

        return f"Error communicating with Ollama: {e}"


# Normal interactive use
if __name__ == "__main__":

    question = input("Ask a question: ")

    answer = answer_question(question)

    print("\nAnswer:")
    print(answer)