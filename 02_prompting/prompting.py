from openai import OpenAI

client = OpenAI()

prompt = """
Explain recursion to a beginner.
Use simple words and give one Java example.
"""

response = client.responses.create(
    model="gpt-5.6-luna",
    input=prompt
)

print(response.output_text)