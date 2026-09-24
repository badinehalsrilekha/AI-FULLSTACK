from ollama import chat
roles=[
    "You are a fashion designer.Answer about it in 4 lines.",
    "You are a docter .Answer about it briefly.",
    "You are a chef .Answer it according to your field"
]
for role in roles:
    response=chat(
    model="llama3.2",
    messages=[
        {
            "role" : "system",
            "content" : role
        },
        {
            "role" : "user",
            "content" : "How  an omlet is prepared?"
        }
    ]
    )
    print(f"--- {role} ---")
    print(response.message.content)
    print()
