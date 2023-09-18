tasks =[]
def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added")

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Task '{task}' removed")

    else:
        print(f"Task '{task}' not found")

def display_tasks():
    if not tasks:
        print("No tasks in list")

    else:
        print("Your tasks are: ")
        for i , task in enumerate(tasks, start=1):
            print(f"{i},{task}")

while True:
    print("\nOptions: ")
    print("1.Add task")
    print("2.Remove task")
    print("3.Display tasks")
    print("4.Quit")

    choice = input("Enter your choice: ")
    if choice =="1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice=="2":
        task = input("Enter the task to remove: ")
        remove_task(task)

    elif choice=="3":
        display_tasks()
    elif choice == "4":
        print("Good bye!")
        break
    else:
        print("Invalid choice.Please try again")