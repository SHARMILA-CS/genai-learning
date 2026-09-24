# Tool 1
def add_numbers(a, b):
    return a + b


# Tool 2
def multiply_numbers(a, b):
    return a * b


# User task
question = input("Enter a task: ")

print("\nTask:", question)


# Agent steps
print("\nAgent is deciding what to do...")

# Step 1: Add the numbers
print("\nTool requested: add_numbers")
print("Arguments: {'a': 10, 'b': 20}")

result1 = add_numbers(10, 20)

print("Tool result:", result1)


# Step 2: Use the result from the first tool
print("\nAgent observes the result:", result1)
print("Agent decides the next action...")


print("\nTool requested: multiply_numbers")
print("Arguments:", {
    "a": result1,
    "b": 3
})

result2 = multiply_numbers(result1, 3)

print("Tool result:", result2)


# Final answer
print("\nFinal answer:")
print(result2)