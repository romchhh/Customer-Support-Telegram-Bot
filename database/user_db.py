import sqlite3
import datetime
from datetime import datetime

current_time = datetime.now()

conn = sqlite3.connect('data/data.db')
cursor = conn.cursor()

def create_table():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            user_name TEXT,
            blocked BOOLEAN DEFAULT 0 CHECK(blocked IN (0, 1))
        )
    ''')
    conn.commit()
    conn.close()


def add_user(user_id, user_name):
    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    existing_user = cursor.fetchone()
    if existing_user is None:
        cursor.execute('''
            INSERT INTO users (user_id, user_name)
            VALUES (?, ?)
        ''', (user_id, user_name))
        conn.commit()
    
    
def create_questions_table():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            manager_id INTEGER,
            user_name TEXT,
            time NUMERIC,
            questions TEXT,
            answers TEXT,
            ended INTEGER  
        )
    ''')
    conn.commit()
    conn.close()    

def add_question_to_db(user_id, user_name, question):
    cursor.execute('SELECT id, questions FROM questions WHERE user_id = ? AND ended = 0 ORDER BY id DESC LIMIT 1', (user_id,))
    row = cursor.fetchone()

    if row:
        # Якщо запис існує, додаємо нове питання через кому
        question_id, existing_questions = row
        updated_questions = f"{existing_questions}, {question}"
        cursor.execute('UPDATE questions SET questions = ? WHERE id = ?', (updated_questions, question_id))
    else:
        # Якщо запису немає, створюємо новий запис
        cursor.execute('''
            INSERT INTO questions (user_id, manager_id, user_name, time, questions, answers, ended)
            VALUES (?, ?, ?, datetime('now'), ?, '', 0)
        ''', (user_id, None, user_name, question))
        question_id = cursor.lastrowid

    conn.commit()

    return question_id



def get_manager_id_from_db(user_id):
    cursor.execute('SELECT manager_id FROM questions WHERE user_id = ? ORDER BY id DESC LIMIT 1', (user_id,))
    manager_id = cursor.fetchone()[0]
    return manager_id


def end_dialog_in_db(question_id):
    cursor.execute('UPDATE questions SET ended = 1 WHERE id = ?', (question_id,))
    conn.commit()
