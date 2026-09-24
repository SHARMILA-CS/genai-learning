import requests
import chromadb
from sentence_transformers import SentenceTransformer

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

    # 7. Send prompt to Gemma through Ollama
    url = "http://localhost:11434/api/generate"

    data = {
        "model": "gemma3:4b",
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.2,
            "num_predict": 150
        }
    }

    # 8. Get LLM response
    response = requests.post(url, json=data)
    response.raise_for_status()

    result = response.json()

    return result["response"]


# Normal interactive use
# Normal interactive use
if __name__ == "__main__":
    question = input("Ask a question: ")

    answer = answer_question(question)

    print("\nAnswer:")
    print(answer)