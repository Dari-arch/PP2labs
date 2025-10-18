from backend.storage_sqlite import get_all_students, get_top_student

def show_top_student():
    top = get_top_student()
    if top:
        print(f"🏆 Top student: {top[0]} | Average: {top[1]:.2f} | Grade: {top[2]}")
    else:
        print("No students found!")

def show_statistics():
    students = get_all_students()
    if not students:
        print("Database is empty!")
        return
    avgs = [s[8] for s in students]
    print(f"📈 Average of all students: {sum(avgs)/len(avgs):.2f}")
