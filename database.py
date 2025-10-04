import sqlite3

DATABASE = 'assistant.db'

def connect_db():
    return sqlite3.connect(DATABASE)

def init_db():
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS memory (
                        key TEXT PRIMARY KEY,
                        value TEXT)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS user_topics (
                        user_id TEXT,
                        topic TEXT)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS feedback (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id TEXT,
                        feedback_text TEXT)''')
    
    conn.commit()
    conn.close()