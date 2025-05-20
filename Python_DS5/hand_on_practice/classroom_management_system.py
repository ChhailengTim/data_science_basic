def add_student(students):
    student_id = input('Enter the student ID: ')
    student_name = input('Enter the student name: ')
    score = float(input('Enter the score: '))
    students[student_id] = {
        "name": student_name,
        "score": score
    }
    print(f'Student {student_name} with score {score:.2f} added successfully.')
    return students

def edit_student(students):
    student_id = input('Enter the student ID to edit: ')
    if student_id in students:
        student_name = input('Enter the new student name: ')
        score = float(input('Enter the new score: '))
        students[student_id] = {
            "name": student_name,
            "score": score
        }
        print(f'Student {student_id} updated successfully.')
        return students
    else:
        print(f'Student ID {student_id} not found.')

def show_students(students):
    if not students:
        print('No students found.')
    else:
        print('Student ID\tName\tScore')
        for student_id, details in students.items():
            print(f'{student_id}\t\t{details["name"]}\t\t{details["score"]:.2f}')

def delete_student(students):
    student_id = input('Enter the student ID to delete: ')
    if student_id in students:
        del students[student_id]
        print(f'Student ID {student_id} deleted successfully.')
    else:
        print(f'Student ID {student_id} not found.')

def compute_average(students):
    if not students:
        print('No students found to compute average.')
        return
    total_score = sum(details["score"] for details in students.values())
    average_score = total_score / len(students)
    print(f'The class average score is : {average_score:.2f}')

    


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
        edit_student(students)
    elif choice == 3:   
        show_students(students)
    elif choice == 4:
        delete_student(students)
    elif choice == 5:
        compute_average(students)
    elif choice == 6:
        print('Exiting the program.')
        break