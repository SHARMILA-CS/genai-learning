import chromadb
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to existing Chroma database
client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_collection(
    name="college_rules"
)

# User question
question = input("Ask a question: ")

# Convert question into an embedding
question_embedding = model.encode(question).tolist()

# Search for similar chunks
results = collection.query(
    query_embeddings=[question_embedding],
    n_results=2
)

print("\nRelevant chunks:\n")

for document in results["documents"][0]:
    print(document)
    print()