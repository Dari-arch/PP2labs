import sqlite3
import os

def create_database():
    # Егер база бұрын бар болса, қайта қолданамыз
    db_path = "students.db"

    # Базамен байланыс орнату (жоқ болса — автоматты түрде жасайды)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Кесте құрылымын жасау
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id TEXT UNIQUE,
        name TEXT NOT NULL,
        math INTEGER,
        physics INTEGER,
        programming INTEGER,
        english INTEGER,
        database_systems INTEGER,
        average REAL,
        grade TEXT
    )
    """)

    conn.commit()
    conn.close()
    print("✅ Database және students кестесі сәтті құрылды!")

# Егер файл тікелей іске қосылса
if __name__ == "__main__":
    create_database()

