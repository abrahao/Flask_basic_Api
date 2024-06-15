# app/models.py
from .db import get_db

def create_user(data):
    db = get_db()
    cursor = db.cursor()
    try:
        cursor.execute("INSERT INTO usuarios (nome, email, idade) VALUES (%s, %s, %s)", 
                       (data['nome'], data['email'], data['idade']))
        db.commit()
        user_id = cursor.lastrowid
        return user_id
    except Exception as e:
        db.rollback()
        raise e
    finally:
        cursor.close()

def get_users():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios")
    users = cursor.fetchall()
    cursor.close()
    return users

def get_user(user_id):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    cursor.close()
    return user

def update_user(user_id, data):
    db = get_db()
    cursor = db.cursor()
    try:
        cursor.execute("UPDATE usuarios SET nome = %s, email = %s, idade = %s WHERE id = %s", 
                       (data['nome'], data['email'], data['idade'], user_id))
        db.commit()
        return cursor.rowcount
    except Exception as e:
        db.rollback()
        raise e
    finally:
        cursor.close()

def delete_user(user_id):
    db = get_db()
    cursor = db.cursor()
    try:
        cursor.execute("DELETE FROM usuarios WHERE id = %s", (user_id,))
        db.commit()
        return cursor.rowcount
    except Exception as e:
        db.rollback()
        raise e
    finally:
        cursor.close()
