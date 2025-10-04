```python
from app import create_app
from app.database import init_db
from app.assistant import ask_customization

def main():
    init_db()
    app = create_app()
    
    print("Welcome to the Flask Assistant!")
    
    assistant = ask_customization()
    print(f"Assistant {assistant.name} is ready to help you out!")

    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("Goodbye! Have a great day!")
            break
        
        response = assistant.handle_chat(user_input)
        print(response['response'])

if __name__ == '__main__':
    main()
```