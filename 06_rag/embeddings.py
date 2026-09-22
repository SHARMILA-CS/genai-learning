from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter

with open("documents/college_rules.txt", "r", encoding="utf-8") as file:
    text = file.read()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=50
)

chunks = splitter.split_text(text)

model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(chunks)

for index, embedding in enumerate(embeddings):
    print(f"\nChunk {index + 1}:")
    print(chunks[index])

    print("Embedding:")
    print(embedding)

    print("Vector dimensions:", len(embedding))