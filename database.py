import sqlite3
import os

# Fetch the database path from an environment variable, with a default value
DATABASE = os.getenv('ASSISTANT_DB_PATH', 'assistant.db')

def connect_db() -> sqlite3.Connection:
    """Establish a connection to the SQLite database.

    Returns:
        sqlite3.Connection: The database connection object.
    """
    return sqlite3.connect(DATABASE)

def init_db() -> None:
    """Initialize the database by creating required tables."""
    try:
        with connect_db() as conn:  # Using a context manager for auto-closing
            cursor = conn.cursor()

            # Create tables
            cursor.execute('''CREATE TABLE IF NOT EXISTS memory (key TEXT PRIMARY KEY, value TEXT)''')
            cursor.execute('''CREATE TABLE IF NOT EXISTS user_topics (user_id TEXT, topic TEXT)''')
            cursor.execute('''CREATE TABLE IF NOT EXISTS feedback (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id TEXT, feedback_text TEXT)''')

            conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")