import random
from .jokes import get_random_joke
from .magic_eight_ball import ask_eight_ball
from .personality import personality_map
from .config import AssistantConfig

class Assistant:
    def __init__(self, name=AssistantConfig.DEFAULT_NAME, gender=AssistantConfig.DEFAULT_GENDER):
        self.name = name
        self.gender = gender
        self.personality = personality_map[AssistantConfig.DEFAULT_PERSONALITY]

    def get_response(self, user_input):
        return f"You said: {user_input}"

    def handle_chat(self, user_input):
        if "8 ball" in user_input.lower():
            response = ask_eight_ball()
            return {"response": f"🎱 {response}"}

        if "joke" in user_input.lower():
            joke = get_random_joke()
            return {"response": joke}
        
        response = self.get_response(user_input)
        return {"response": f"{self.name}: {self.personality} {response}"}

def ask_customization():
    name = AssistantConfig.DEFAULT_NAME
    gender = AssistantConfig.DEFAULT_GENDER

    print(f"Current Assistant Name: {name}")
    print(f"Current Assistant Gender: {gender}")

    change_name = input("Do you want to change the assistant's name? (yes/no): ").strip().lower()
    if change_name == "yes":
        name = input("Enter a new name for the assistant: ").strip()

    change_gender = input("Do you want to change the assistant's gender? (yes/no): ").strip().lower()
    if change_gender == "yes":
        gender_input = input("Enter 'male' or 'female': ").strip().lower()
        if gender_input in ['male', 'female']:
            gender = gender_input
        else:
            print("Invalid input, keeping the default gender.")

    return Assistant(name, gender)