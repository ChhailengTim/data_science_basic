def add_student(classroom):
    student_name = input("Enter the student's name: ")
    score = eval(input("Enter" + student_name + "'s score: "))
    classroom[student_name] = score
    print("Student", student_name, "with score", score, "added successfully.\n")
    return classroom

def edit_student(classroom):
    student_name = input("Enter the student's name to edit: ")
    if student_name in classroom:
        new_score = eval(input("Enter the new score for" + student_name + ": "))
        classroom[student_name] = new_score
        print("Updated", student_name + "'s score to", new_score, ".\n")
    else:
        print(student_name, "not found.\n")
    return classroom

def show_students(classroom):
    if classroom:
        print("Students and their scores:")
        for student, score in classroom.items():
            print(student, ":", score)
        print()
    else:
        print("No students in the classroom.\n")
    return classroom

def delete_student(classroom):
    student_name = input("Enter the student's name to delete: ")
    if student_name in classroom:
        del classroom[student_name]
        print(student_name, "deleted successfully.\n")
    else:
        print(student_name, "not found.\n")
    return classroom

def compute_average(classroom):
    if classroom:
        total_score = sum(classroom.values())
        class_size = len(classroom)
        average_score = total_score / class_size
        print("The class average score is:", round(average_score, 2), "\n")
    else:
        print("No students in the classroom to compute the average.\n")
    return classroom

# Main program loop
classroom = {}

while True:
    print("\nClassroom Management Menu:")
    print("1. Add Student and Score")
    print("2. Edit Student Record")
    print("3. Show All Students and Scores")
    print("4. Delete Student Record")
    print("5. Compute Class Average")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        classroom = add_student(classroom)
    elif choice == '2':
        classroom = edit_student(classroom)
    elif choice == '3':
        classroom = show_students(classroom)
    elif choice == '4':
        classroom = delete_student(classroom)
    elif choice == '5':
        classroom = compute_average(classroom)
    elif choice == '6':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1-6).\n")
