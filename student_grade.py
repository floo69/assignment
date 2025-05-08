def manage_grades():
    grades = {}

    while True:
        print("\n1. Add/Update Student Grade")
        print("2. Print All Student Grades")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter student name: ")
            grade = input("Enter grade: ")
            grades[name] = grade
            print(f"Grade for {name} updated to {grade}.")

        elif choice == "2":
            if not grades:
                print("No grades recorded.")
            else:
                for name, grade in grades.items():
                    print(f"{name}: {grade}")

        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

manage_grades()
