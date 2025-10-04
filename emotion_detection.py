```python
def detect_emotion(user_input):
    positive_words = ["good", "great", "happy", "excited", "love"]
    negative_words = ["bad", "sad", "angry", "hate", "tired"]
    
    if any(word in user_input.lower() for word in positive_words):
        return "positive"
    elif any(word in user_input.lower() for word in negative_words):
        return "negative"
    else:
        return "neutral"
```