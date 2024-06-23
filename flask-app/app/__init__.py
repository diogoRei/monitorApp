from flask import Flask
import sqlite3

DATABASE = './storage.db'
WTF_CSRF_SECRET_KEY = '168428DIOGOREIS'

app = Flask(__name__)
app.config['SECRET_KEY'] = WTF_CSRF_SECRET_KEY
app.config['RECAPTCHA_PUBLIC_KEY']='6LevsP8pAAAAALGrywJHNLMn8fnu99ZMNuZ9FOcC'
app.config['RECAPTCHA_PRIVATE_KEY']='6LevsP8pAAAAAOZZfu-NOaw8dijsX0aa9xyp8iRJ'
app.config['RECAPTCHA_DATA_ATTRS']= {'theme': 'dark'}

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

