import ollama
response = ollama.chat(
    model="llama3.2:3b",
    messages =[
        {
            "role": "system",
            "content": "Give answers in two lines only I am teacher of 5 years old kid."
        },
        {
            "role": "user",
            "content": "explain ai"
        }
    ]
)
print(response["message"]["content"])