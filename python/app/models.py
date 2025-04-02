# app/models.py
from app.db import get_connection

def get_all_memories(user_id: int):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM memories WHERE user_id = %s", (user_id,))
    memories = cursor.fetchall()
    cursor.close()
    conn.close()
    return memories

def get_character_prompt(user_id: int):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT system_prompt FROM characters WHERE user_id = %s", (user_id,))
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    return row["system_prompt"] if row else "너는 고인의 말투로 따뜻하게 대답해줘."

def get_character_info(user_id: int) -> dict:
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM characters WHERE user_id = %s", (user_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def create_character(character: dict):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO characters (name, age, gender, relationship, calling, tone, personality, dialect, belief, habit_phrases, hobbies, death_year)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        character['name'],
        character['age'],
        character['gender'],
        character['relationship'],
        character['calling'],
        character['tone'],
        character['personality'],
        character['dialect'],
        character['belief'],
        character['habit_phrases'],
        character['hobbies'],
        character['death_year']
    ))
    conn.commit()
    cursor.close()
    conn.close()
    return character

def save_memory(memory: dict):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO memories (user_id, content, date, location, keywords, emotion)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        memory['user_id'],
        memory['content'],
        memory['date'],
        memory['location'],
        memory['keywords'],
        memory['emotion']
    ))
    conn.commit()
    cursor.close()
    conn.close()
    return memory