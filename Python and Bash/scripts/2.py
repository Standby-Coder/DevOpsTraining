def add():
    try:
        name = input("Enter student's name: ")
        grade = float(input("Enter student's grade: "))
        if name in gradeList:
            raise ValueError("Student already exists.")
        if not (0 <= grade <= 100):
            raise ValueError("Grade must be between 0 and 100.")
        gradeList[name] = grade
        print(f"Added {name} with grade {grade}.")
    except ValueError as e:
        print("Error: " + str(e))

def updateGrade():
    try:
        name = input("Enter student's name to update grade: ")
        if name not in gradeList:
            raise ValueError("Student does not exist.")
        new_grade = float(input("Enter new grade: "))
        if not (0 <= new_grade <= 100):
            raise ValueError("Grade must be between 0 and 100.")
        gradeList[name] = new_grade
        print(f"Updated {name}'s grade to {new_grade}.")
    except ValueError as e:
        print("Error: " + str(e))

def viewAll():
    if not gradeList:
        print("No students found.")
    else:
        print("Students and their grades:")
        for name, grade in gradeList.items():
            print(f"{name}: {grade}")

if __name__ == "__main__":
    gradeList = {}
    while True:
        try:
            print("-" * 20)
            print("Enter a choice:")
            print("1. Add new student and grade")
            print("2. Update student's grade")
            print("3. View all students and grades")
            print("4. Exit")
            choice = int(input("Choice: "))
            if choice == 1:
                add()
            elif choice == 2:
                updateGrade()
            elif choice == 3:
                viewAll()
            elif choice == 4:
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError as e:
            print("Error: " + str(e))