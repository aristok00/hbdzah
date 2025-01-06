from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Buat atau sambungkan ke database SQLite
DB_NAME = 'database.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS wishes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            wish TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/save', methods=['POST'])
def save_wish():
    data = request.get_json()
    wish = data.get('wish')

    if not wish:
        return jsonify({'error': 'Wish cannot be empty'}), 400

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO wishes (wish) VALUES (?)', (wish,))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Wish saved successfully'}), 200

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
