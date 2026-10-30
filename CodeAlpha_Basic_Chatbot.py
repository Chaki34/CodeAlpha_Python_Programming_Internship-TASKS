
import re


def normalize_message(message):
    """Convert messages to lowercase and remove punctuation."""
    message = message.lower().strip()
    message = re.sub(r"[^\w\s]", "", message)
    message = re.sub(r"\s+", " ", message)
    return message


def show_welcome():
    print("\n" + "=" * 55)
    print("                 BASIC CHATBOT")
    print("          CodeAlpha Python Internship")
    print("=" * 55)
    print("Hello! I am your Python chatbot.")
    print("Type 'help' to see what you can ask me.")
    print("Type 'bye' or 'exit' to end the conversation.")
    print("=" * 55)


def show_help():
    print("\nHere are 10 types of questions you can ask me:")
    print("-" * 55)

    questions = [
        "1. Hello / Hi / Hey",
        "2. How are you?",
        "3. What is your name?",
        "4. Tell me about you.",
        "5. Who created you?",
        "6. What can you do?",
        "7. What is Python?",
        "8. What is programming?",
        "9. What is your purpose?",
        "10. What is your favourite language?"
    ]

    for question in questions:
        print(question)

    print("\nYou can also type 'help' to view this list.")
    print("Type 'bye' or 'exit' to close the chatbot.")
    print("-" * 55)


def get_response(user_message):

    message = normalize_message(user_message)

    # 1. Greetings
    if message in [
        "hi", "hello", "hey", "hii",
        "good morning", "good afternoon", "good evening"
    ]:
        return "Hello! Nice to meet you. How can I help you?"

    # 2. How are you?
    elif message in [
        "how are you", "how are you doing",
        "are you fine", "are you okay"
    ]:
        return "I'm fine, thank you for asking! How are you?"

    # 3. Chatbot name
    elif message in [
        "what is your name", "your name", "who are you"
    ]:
        return "I am Basic Chatbot, a simple rule-based Python chatbot."

    # 4. About the chatbot
    elif message in [
        "tell me about you", "about you",
        "tell me about yourself", "introduce yourself"
    ]:
        return (
            "I am Basic Chatbot, a console-based chatbot developed "
            "using Python. I can answer predefined questions, "
            "respond to greetings, and provide basic information "
            "through rule-based conversation."
        )

    # 5. Creator information
    elif message in [
        "who created you",
        "who create you",
        "who crated you",
        "who is your creator",
        "who developed you",
        "who develop you",
        "who made you",
        "who is your developer"
    ]:
        return (
            "I was created by Debmalya Chaki, a B.Tech Computer "
            "Science and Engineering student, as part of the "
            "CodeAlpha Python Programming Internship."
        )

    # 6. Capabilities
    elif message in [
        "what can you do", "your capabilities", "what do you do"
    ]:
        return (
            "I can respond to greetings, answer 10 categories of "
            "predefined questions, share information about myself "
            "and my creator, and display a help menu."
        )

    # 7. Python
    elif message in [
        "what is python", "define python", "tell me about python"
    ]:
        return (
            "Python is a high-level, interpreted programming "
            "language known for its simple syntax and readability."
        )

    # 8. Programming
    elif message in [
        "what is programming", "define programming",
        "tell me about programming"
    ]:
        return (
            "Programming is the process of writing instructions "
            "that tell a computer how to perform specific tasks."
        )

    # 9. Purpose
    elif message in [
        "what is your purpose", "your purpose",
        "why were you created"
    ]:
        return (
            "My purpose is to demonstrate basic chatbot development "
            "using Python concepts such as functions, loops, "
            "conditional statements, and user input."
        )

    # 10. Favourite language
    elif message in [
        "what is your favourite language",
        "which language do you like",
        "your favourite programming language"
    ]:
        return (
            "I am built using Python, so Python is my favourite "
            "programming language!"
        )

    # Additional question: CodeAlpha
    elif message in [
        "what is codealpha",
        "tell me about codealpha",
        "which internship is this"
    ]:
        return (
            "This project is part of the CodeAlpha Python "
            "Programming Internship, where I am practising "
            "Python programming through practical projects."
        )

    # Help menu
    elif message in [
        "help", "menu", "questions", "what can i ask"
    ]:
        show_help()
        return "Feel free to ask me any of these questions!"

    # Unknown question
    else:
        return (
            "Sorry, I don't understand that question yet.\n"
            "Please type 'help' to see the available questions."
        )


def chatbot():

    show_welcome()

    while True:

        user_message = input("\nYou: ").strip()

        if not user_message:
            print("Bot: Please enter a message.")
            continue

        message = normalize_message(user_message)

        # Exit commands
        if message in [
            "bye", "goodbye", "exit", "quit",
            "see you", "good bye"
        ]:
            print("\nBot: Goodbye! Thank you for chatting with me.")
            print("Bot: Have a wonderful day!")
            break

        response = get_response(user_message)

        print("\nBot:", response)


if __name__ == "__main__":
    chatbot()
