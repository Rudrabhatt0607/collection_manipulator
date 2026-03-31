students = {}

print("Welcome to the Student Data Organizer!")

while True:

    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nEnter student details:")
        sid = int(input("Student ID: "))
        name = input("Name: ")
        age = int(input("Age: "))
        grade = input("Grade: ")
        sub = input("Enter subjects (comma): ")

        subjects = sub.split(",")

        students[sid] = {
            "name": name,
            "age": age,
            "grade": grade,
            "subjects": subjects
        }

        print("Student added successfully!")

    elif choice == "2":
        print("\nAll Students:")
        for sid, data in students.items():
            print(f"\nID: {sid}")
            print(f"Name: {data['name']}")
            print(f"Age: {data['age']}")
            print(f"Grade: {data['grade']}")
            print("Subjects:", data["subjects"])

    elif choice == "3":
        sid = int(input("Enter student ID to update: "))
        if sid in students:
            name = input("New Name: ")
            age = int(input("New Age: "))
            students[sid]["name"] = name
            students[sid]["age"] = age
            print("Student updated!")
        else:
            print("Student not found")

    elif choice == "4":
        sid = int(input("Enter student ID to delete: "))
        if sid in students:
            del students[sid]
            print("Student deleted")
        else:
            print("Student not found")

    elif choice == "5":
        all_subjects = set()
        for data in students.values():
            all_subjects.update(data["subjects"])

        print("Subjects Offered:", all_subjects)

    elif choice == "6":
        print("Thank you for using the Student Data Organizer!")
        break

    else:
        print("Invalid choice")