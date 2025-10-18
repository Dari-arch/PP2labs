from backend.storage_sqlite import get_all_students

def export_results():
    students = get_all_students()
    with open("results.txt", "w", encoding="utf-8") as f:
        for s in students:
            f.write(f"{s[1]}, {s[2]}, {s[8]:.2f}, {s[9]}\n")
    print("💾 Results exported to results.txt")
