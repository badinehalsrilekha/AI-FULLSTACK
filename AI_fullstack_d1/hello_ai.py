from ollama import chat
response=chat(
    model="llama3.2",
    messages=[
        {
            "role" : "user",
            "content" : "What is the use of javascript?"
        }
    ]
)
print(response.message.content)