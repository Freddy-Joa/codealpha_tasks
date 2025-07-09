# Intermediate chatbot with improved handling

def chatbot():
    print("Warm welcome !!! \n lets start the conversation ...\n type hello to start \n Type 'help' for options or 'bye' to exit.")

    while True:
        quer = input("You: ").strip().lower()

        if quer == "hello":
            print("Alphabot: Hi there! welcome back")
        elif quer == "how are you":
            print("Alphabot: I'm great, thanks for asking!")
        elif quer == "what can you do":
            print("Alphabot: I can say hello , chat some , and say goodbye. Try typing 'help'!")
        elif quer == "help":
            print("Alphabot: Available commands: hello, how are you, what can you do, bye")
        elif quer == "bye":
            print("Alphabot: Goodbye! Have a wonderful day! ")
            break
        else:
            print("Bot: Hmm, I don’t recognize that. Try <help> for options!")

chatbot()