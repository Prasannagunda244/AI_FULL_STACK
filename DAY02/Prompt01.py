import ollama
response = ollama.chat(
    model="llama3.2:3b",
    messages =[
        {
            "role": "user",
            "content": "Give the defination of AI in two lines"
        }
    ]
)
print(response["message"]["content"])