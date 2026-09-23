import ollama
response = ollama.chat(
    model="llama3.2:3b",
    messages =[
        {
            "role": "system",
            "content": "Give answer in two lines only"
        },
        {
            "role": "user",
            "content": "explain ai"
        }
    ]
)
print(response["message"]["content"])