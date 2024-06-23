from app import app, get_db_connection
from flask import request, jsonify, render_template

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    conn.close()

    if cursor.rowcount == 0:
        return jsonify({'error': 'User not found'}), 404

    return '', 204