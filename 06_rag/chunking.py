from langchain_text_splitters import RecursiveCharacterTextSplitter

with open("documents/college_rules.txt", "r", encoding="utf-8") as file:
    text = file.read()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=50
)

chunks = splitter.split_text(text)

for index, chunk in enumerate(chunks):
    print(f"\n--- Chunk {index + 1} ---")
    print(chunk)