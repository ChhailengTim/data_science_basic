def add_task(todo_dict):
    task_id = len(todo_dict) + 1  # Generate task ID
    task = input("Enter the task you want to add: ")
    todo_dict[task_id] = task
    print("Task", task, "has been added with ID", task_id, ".\n")
    return todo_dict

def edit_task(todo_dict):
    show_tasks(todo_dict)
    task_id = eval(input("Enter the ID of the task you want to edit: "))

    if task_id in todo_dict:
        new_task = input("Enter the new task: ")
        todo_dict[task_id] = new_task
        print("Task with ID", task_id, "has been updated to:", new_task, "\n")
    else:
        print("Invalid task ID.\n")
    return todo_dict

def show_tasks(todo_dict):
    if todo_dict:
        print("Here are your tasks:")
        print("ID\t Task")
        for task_id, task in todo_dict.items():
            print(task_id, "\t", task)
        print()
    else:
        print("Your To-Do list is empty.\n")
    return todo_dict

def clear_tasks(todo_dict):
    todo_dict.clear()
    print("All tasks have been cleared from your To-Do list.\n")
    return todo_dict

# Main program loop
todo_dict = {}

while True:
    print("To-Do List Menu:")
    print("1. Add Task")
    print("2. Edit Task")
    print("3. Show Tasks")
    print("4. Clear Tasks")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        todo_dict = add_task(todo_dict)
    elif choice == '2':
        todo_dict = edit_task(todo_dict)
    elif choice == '3':
        todo_dict = show_tasks(todo_dict)
    elif choice == '4':
        todo_dict = clear_tasks(todo_dict)
    elif choice == '5':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1-5).\n")
