import random

responses = [
    "Yes, definitely!",
    "Ask again later.",
    "No way!",
    "Absolutely!",
    "I wouldn't count on it.",
    "Yes!",
    "My sources say no.",
    "Very likely.",
    "Don't hold your breath.",
    "Cannot predict now.",
]

def ask_eight_ball():
    return random.choice(responses)