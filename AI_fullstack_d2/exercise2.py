from ollama import chat

messages = [
    {"role" : "system", "content" : "Turn a plain commpliment into an exaggerated over-the-top one."},
    
    {"role" : "user" , "content": "You did a good job"},
    {"role" : "system", "content": "You didn't just do a good job, you basically redifined what 'good' means to the rest of us"},

    {"role" : "user" , "content": "Nice haircut"},
    {"role" : "system", "content": "That haircut is so good,the barbers are going to study it in text books"},

    {"role" : "user" , "content": "Good game."}
]

response = chat(
    model = "llama3.2",
    messages = messages
)

print(response.message.content)