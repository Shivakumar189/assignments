# Assignment: Student Data Manager (19/02/2026)
# Store data for 5 students, find topper, class average, and assign grades

def assign_grade(marks: float) -> str:
    """Assign a letter grade based on marks out of 100."""
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

def main():
    # Student data: list of dictionaries
    students = [
        {"name": "Aarav",   "marks": 92},
        {"name": "Priya",   "marks": 78},
        {"name": "Rahul",   "marks": 85},
        {"name": "Sneha",   "marks": 60},
        {"name": "Vikram",  "marks": 45},
    ]

    # Assign grades
    for student in students:
        student["grade"] = assign_grade(student["marks"])

    # Find topper
    topper = max(students, key=lambda s: s["marks"])

    # Class average
    average = sum(s["marks"] for s in students) / len(students)

    # Display results
    print("=" * 50)
    print("         📚 Student Data Manager")
    print("=" * 50)
    print(f"{'Name':<12} {'Marks':>6} {'Grade':>6}")
    print("-" * 28)
    for s in students:
        print(f"{s['name']:<12} {s['marks']:>6} {s['grade']:>6}")

    print("-" * 28)
    print(f"\n🏆 Class Topper : {topper['name']} ({topper['marks']} marks)")
    print(f"📊 Class Average: {average:.2f}")
    print("=" * 50)

if __name__ == "__main__":
    main()
