from flask import Flask
import sqlite3

DATABASE = './storage.db'
WTF_CSRF_SECRET_KEY = '168428DIOGOREIS'

app = Flask(__name__)
app.config['SECRET_KEY'] = WTF_CSRF_SECRET_KEY


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')
    
    conn.commit()
    conn.close()


from app.controllers import default

