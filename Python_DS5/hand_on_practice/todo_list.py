tasks = []
while True:
    print('To-Do List Menu:')
    print('1. Add a task')
    print('2. Edit a task')
    print('3. Show tasks')
    print('4. Clear tasks')
    print('5. Exit')
    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        task = input('Enter a task: ')
        tasks.append(task)
    
    elif choice == '2':
        task = input('Enter the task to edit: ')
        if  task in tasks:
            new_task = input('Enter the new task: ')
            index = tasks.index(task)
            tasks[index] = new_task
        else:
            print('Task not found.')
    
    elif choice == '3':
        if len(tasks) == 0:
            print('No tasks available.')
        else:
            print('Tasks:')
            for i, task in enumerate(tasks):
                print(f'{i+1}. {task}')
            print('Total tasks:', len(tasks))
            
    elif choice == '4':
        tasks.clear()
        print('All tasks cleared.')
    
    elif choice == '5':
        print('Exiting the program.')
        break
    else:
        print('Invalid choice. Please enter a number from 1 to 5.')