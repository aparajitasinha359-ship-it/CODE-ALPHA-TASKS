def chatbot_response(user_input):
    message = user_input.lower().strip()

    if message in ("hello", "hi", "hey"):
        return "Hello! How can I help you?"
    elif "how are you" in message:
        return "I'm doing well. Thanks for asking!"
    elif "your name" in message:
        return "I'm a simple Python chatbot."
    elif message == "help":
        return "You can greet me, ask how I am, or say bye."
    elif message in ("bye", "goodbye", "exit", "quit"):
        return "Goodbye! Have a great day."
    else:
        return "Sorry, I don't understand that. Type 'help' to see what I can do."

def main():
    print("===== SIMPLE CHATBOT =====")
    print("Type 'help' for options or 'bye' to exit.")

    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Bot:", response)

        if user_input.lower().strip() in ("bye", "goodbye", "exit", "quit"):
            break

if __name__ == "__main__":
    main()
