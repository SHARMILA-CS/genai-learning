text = input("Enter some text: ")

prompt = f"""
You are an AI text analyzer.

Analyze the following text and provide:

1. A short summary
2. The sentiment
3. Three key points
4. The category of the text
5. Five important keywords

Text:
{text}
"""

print("\nGenerated Prompt:\n")
print(prompt)