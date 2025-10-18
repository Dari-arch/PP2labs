from backend.init_db import create_database
from backend.storage_sqlite import get_all_students, delete_student
from logic.analytics import show_top_student, show_statistics
from backend.seed import generate_students
from ui.export import export_results

def menu():
    create_database()
    while True:
        print("\n--- STUDENT RESULT MANAGEMENT ---")
        print("1. Generate 50 students")
        print("2. Show all students")
        print("3. Show top student")
        print("4. Show statistics")
        print("5. Delete student")
        print("6. Export results to file")
        print("7. Exit")

        choice = input("Choose: ")

        if choice == "1":
            generate_students()
        elif choice == "2":
            students = get_all_students()
            for s in students:
                print(s)
        elif choice == "3":
            show_top_student()
        elif choice == "4":
            show_statistics()
        elif choice == "5":
            sid = input("Enter student ID to delete: ")
            delete_student(sid)
            print("✅ Student deleted.")
        elif choice == "6":
            export_results()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    menu()
