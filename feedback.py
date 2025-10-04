```python
from .database import connect_db

def store_feedback(user_id, feedback_text):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO feedback (user_id, feedback_text) VALUES (?, ?)", (user_id, feedback_text))
    conn.commit()
    conn.close()
```