import random
from logic.grading import calculate_grade
from backend.storage_sqlite import add_student
from backend.init_db import create_database

def generate_students():
    create_database()
    names = ["Ainur", "Diana", "Arman", "Madina", "Nursultan", "Aliya", "Aruzhan", "Dias", "Miras", "Kamila"]
    for i in range(50):
        name = random.choice(names) + str(i)
        marks = [random.randint(40, 100) for _ in range(5)]
        avg = sum(marks) / 5
        grade = calculate_grade(avg)
        add_student(("S"+str(i+1).zfill(3), name, *marks, avg, grade))
    print("✅ 50 students added successfully!")

if __name__ == "__main__":
    generate_students()
