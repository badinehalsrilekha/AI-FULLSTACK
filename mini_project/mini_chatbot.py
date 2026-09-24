from ollama import chat
system_msg= "You are a mom .Give me answer how our mom speaks in one line"
history = [{"role" : "system","content" : system_msg}]
question_counter=0
print("Welcmoe to CandyyBot❤️")
while True:
    question=input("You:")
    if question == " ":
        print("Candyy🐶: Ask something!!")
        continue
    if question.lower().strip() == "/history":
        print("---- Your Conversation so far ----")
        if len(history) < 2:
            print("Nothing so far!!")
        for msg in history[1:]:
            if msg["role"]== "user":
                speaker= "You"
            else:
                speaker = "Candyy🐶"
            print(f"{speaker} : {msg["content"]}")
            print("-----------------")
            print()
    if question.lower().strip()== "/clear":
        history = [{"role" : "system" , "content" : system_msg}]
        print("Your history has been cleared")
        print()
        continue
    if question.lower().strip() == "/help":
        print("----Available Commands------")
        print("/history - display conversation history")
        print("/clear - clears chat history")
        print("/help - displays the list")
        print("exit - quits the chatbot")
        print("--------------------")
        print()
        continue
    if question.lower().strip().startswith("/personality"):
        personality = input("Enter personality: ")
        system_msg = personality
        history = [{"role": "system", "content": system_msg}]
        print("Personality changed successfully!!")
        continue

    if question.lower().strip() == "exit":
        print("Candyy🐶: Byeee Bangarammmmm 🐷😭")
        print(f"You asked {question_counter} questions today....")
        break
    history.append({"role" : "user" , "content" : question})
    question_counter+=1
    try:
        response = chat(
            model="llama3.2",
            messages=history
        )
        reply = response.message.content
        history.append({"role" : "assistant" , "content" : reply})
        print(f"Candyy🐶 :{reply}")
        print()
    except Exception as e:
        print("Unknown issue. Is ollama running?")
