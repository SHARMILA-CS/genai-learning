from rag import answer_question


evaluation_data = [
    {
        "question": "What should students carry inside the campus?",
        "expected_keywords": ["identity card"]
    },
    {
        "question": "What is the salary package?",
        "expected_keywords": ["I don't know"]
    }
]


print("RAG Evaluation\n")

for item in evaluation_data:

    question = item["question"]
    expected_keywords = item["expected_keywords"]

    actual = answer_question(question)

    actual_lower = actual.lower()

    passed = all(
        keyword.lower() in actual_lower
        for keyword in expected_keywords
    )

    print("Question:", question)
    print("Actual:", actual)
    print("Result:", "PASS" if passed else "FAIL")
    print("-" * 60)