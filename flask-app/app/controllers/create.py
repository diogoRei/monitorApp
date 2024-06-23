from app import app, get_db_connection
from flask import request, jsonify, render_template

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data['name']
    email = data['email']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
    conn.commit()
    conn.close()

    return jsonify({'id': cursor.lastrowid, 'name': name, 'email': email}), 201