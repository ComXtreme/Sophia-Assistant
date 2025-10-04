# Sophia Assistant

A customizable virtual assistant built with Flask.

## Features
- Personality Variability
- Gender and Name Customization
- Joke Implementation
- 8 Ball Game Response
- Simple interaction in a console
- Placeholder for emotion and feedback features

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd flask_assistant
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the server:**

   ```bash
   python run.py
   ```

5. **Customize your Assistant:**
   Upon running the server, you'll be prompted to customize the assistant's name and gender. You can choose to keep the defaults or set your own preferences.

6. **Start Chatting:**
   Type your message directly into the console. To use the 8 Ball, include "8 ball" in your message.

   ```
   You: 8 ball, will I have a good day?
   Assistant: 🎱 Yes, definitely!
   ```

   You can continue the conversation until you type `exit`.
