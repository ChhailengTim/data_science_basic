def add_student(students):
    student_id = input('Enter the student ID:')
    student_name = input('Enter the student name:')
    score = float(input('Enter the score:'))
    students[student_id] = {
        "name": student_name,
        "score": score
    }
    print(f'Student {student_name} with score {score:.2f} added successfully.')
    return students

students = {}

while True:
    print('Classroom Management Menu:')
    print('1. Add Student and Score')
    print('2. Edit Student Record')
    print('3. Show All Students and Scores')
    print('4. Delete Student Record')
    print('5. Compute Class Average')
    print('6. Exit')
    choice = eval(input('Enter your choice (1-6):'))
    if choice == 1:
        add_student(students)
    elif choice == 2:
        None
    elif choice == 3:   
        None
    elif choice == 4:
        None
    elif choice == 5:
        None
    elif choice == 6:
        print('Exiting the program.')
        break