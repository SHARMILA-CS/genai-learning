with open("documents/college_rules.txt", "r", encoding="utf-8") as file:
    text = file.read()

chunk_size = 100

chunks = []

for i in range(0, len(text), chunk_size):
    chunk = text[i:i + chunk_size]
    chunks.append(chunk)

for index, chunk in enumerate(chunks):
    print(f"\n--- Chunk {index + 1} ---")
    print(chunk)