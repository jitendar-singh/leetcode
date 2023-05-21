import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1! How can I assist you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"how are you ?",
        ["I'm good. How about you?",]
    ],
    [
        r"sorry (.*)",
        ["No problem", "Don't worry about it",]
    ],
    [
        r"quit",
        ["Goodbye! Take care.",]
    ],
]

def chatbot():
    print("Hello! How can I help you today?")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    nltk.download("punkt")
    chatbot()
