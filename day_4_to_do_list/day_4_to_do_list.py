#project for app console
tasks=[]
def add_task():
    global tasks
    task=input("Enter a task:")
    tasks.append(task)
def view_tasks():
    global tasks
    if len(tasks)==0:
        print("No tasks available.")
    else:
        print("Here are your tasks:")
        for i ,task in enumerate(tasks,start=1):
            print(f"{i}. {task}")
def remove_task():
    global tasks
    if len(tasks)==0:
        print("No tasks to remove.")
    else:
        view_tasks()
        task_to_remove=int(input("Enter task number you want to remove :"))
        if task_to_remove>0 and task_to_remove<=len(tasks):
            tasks.pop(task_to_remove-1)
            print("Total tasks now:",len(tasks))
        elif task_to_remove>len(tasks) or task_to_remove<1:
            print("Please enter a number present in list")
            remove_task()
        else:
            print("Please enter a number.")
            remove_task()
def mark_completed():
    global tasks
    if len(tasks)==0:
        print("No tasks to mark as completed.")
    else:
        view_tasks()
        completed=int(input("Enter task number you want to marks as completed :"))
        if completed>0 and completed<=len(tasks):
            tasks[completed-1]=f"[✓] {tasks[completed-1]}"
        else:
            print("Task is not present in list.")
def clear_tasks():
    global tasks
    if len(tasks)==0:
        print("Tasks are already empty")
    else:
        tasks.clear()
        view_tasks()
def menu():
    print("========= TO-DO LIST =========")
    choice = int(input("1. Add Task\n2. View Tasks\n3. Remove Task\n4. Mark Task as Completed\n5. Clear Entire Tasks\n6. Exit\nChoose a number: "))
    if choice >6 or choice <1:
        print("Invalid choice.Please select a valid number .")
        menu()
    else:
        if choice == 1:
            add_task()
        elif choice==2:
            view_tasks()
        elif choice==3:
            remove_task()
        elif choice==4:
            mark_completed()
        elif choice==5:
            clear_tasks()
        else:
            print("Thank you for visiting\nExiting program...")
            exit()
while True:
    menu()