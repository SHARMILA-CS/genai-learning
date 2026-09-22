import chromadb
from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 1. Load document
with open("documents/college_rules.txt", "r", encoding="utf-8") as file:
    text = file.read()

# 2. Split document into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=50
)

chunks = splitter.split_text(text)

# 3. Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# 4. Create embeddings
embeddings = model.encode(chunks).tolist()

# 5. Create local Chroma database
client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_or_create_collection(
    name="college_rules"
)

# 6. Store chunks + embeddings
collection.add(
    ids=[f"chunk_{i}" for i in range(len(chunks))],
    documents=chunks,
    embeddings=embeddings
)

print("Stored", len(chunks), "chunks in Chroma.")