from app import app, get_db_connection
from flask import request, jsonify, render_template

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    name = data['name']
    email = data['email']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET name = ?, email = ? WHERE id = ?', (name, email, user_id))
    conn.commit()
    conn.close()

    if cursor.rowcount == 0:
        return jsonify({'error': 'User not found'}), 404

    return jsonify({'id': user_id, 'name': name, 'email': email})