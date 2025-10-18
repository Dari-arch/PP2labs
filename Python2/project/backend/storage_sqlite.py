import sqlite3

def connect_db():
    return sqlite3.connect("students.db")

def add_student(student):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO students (student_id, name, math, physics, programming, english, database_systems, average, grade)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, student)
    conn.commit()
    conn.close()

def get_all_students():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_student(student_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE student_id=?", (student_id,))
    conn.commit()
    conn.close()

def get_top_student():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT name, average, grade FROM students ORDER BY average DESC LIMIT 1")
    top = cursor.fetchone()
    conn.close()
    return top
