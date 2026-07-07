import sqlite3
import os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), 'futuremap.db')

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # Returns dict-like rows
    return conn

def init_db():
    """Create tables if they don't exist"""
    conn = get_connection()
    cursor = conn.cursor()

    # Users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            skills TEXT DEFAULT '',
            joined TEXT DEFAULT CURRENT_DATE
        )
    ''')

    # Predictions table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_name TEXT NOT NULL,
            skills TEXT NOT NULL,
            recommended_career TEXT NOT NULL,
            confidence TEXT NOT NULL,
            date TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()
    print("Database initialized: futuremap.db")

# ===== USER FUNCTIONS =====
def create_user(name, email, password, skills=''):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            'INSERT INTO users (name, email, password, skills, joined) VALUES (?, ?, ?, ?, ?)',
            (name, email, password, skills, datetime.now().strftime('%Y-%m-%d'))
        )
        conn.commit()
        user_id = cursor.lastrowid
        conn.close()
        return {'id': user_id, 'name': name, 'email': email}
    except sqlite3.IntegrityError:
        conn.close()
        return None  # Email already exists

def get_user_by_email(email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return dict(row)
    return None

def get_user_by_id(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return dict(row)
    return None

# ===== PREDICTION FUNCTIONS =====
def save_prediction(user_name, skills, recommended_career, confidence):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO predictions (user_name, skills, recommended_career, confidence, date) VALUES (?, ?, ?, ?, ?)',
        (user_name, skills, recommended_career, confidence, datetime.now().strftime('%Y-%m-%d %H:%M'))
    )
    conn.commit()
    pred_id = cursor.lastrowid
    conn.close()
    return pred_id

def get_all_predictions():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM predictions ORDER BY id DESC LIMIT 50')
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def get_prediction_count():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) as count FROM predictions')
    row = cursor.fetchone()
    conn.close()
    return row['count']

# Initialize DB on import
init_db()
