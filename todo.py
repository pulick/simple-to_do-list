todo = []

def todoli():
    user = input("Please enter the task: ")
    todo.append(user)
    print(todo)

def remove():
    task = input("Please enter the task you have completed: ")
    if task in todo:
        todo.remove(task)
    else:
        print("Task not found in the list.")

def display():
    print(todo)

def mainloop():
    while True:
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            todoli()
        elif choice == '2':
            remove()
        elif choice == '3':
            display()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

mainloop()
