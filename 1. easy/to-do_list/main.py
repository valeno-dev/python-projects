
def show_menu():
    print("\n==== TO-DO LIST MENU ====")
    print("1. View all tasks")
    print("2. Add a new task")
    print("3. Mark a task as done")
    print("4. Delete a task")
    print("5. Exit")
    print("=========================")

def show_tasks(x):
    if len(x) == 0:
        print("You need to add a task first!")
    else:
        print("\n")
        print(f"\nTotal tasks: {len(x)}\n")
        for i, task in enumerate(x, start=1):
            status = "✅" if task["done"] == True else "❌"
            print(f"{i}. {task['name']} - {status}")

def add_task(x):
    task = input("\nEnter a task: ").strip()
    if not task:
        print("⚠️  Task cannot be empty!")
        return
    x.append({"name": task, "done": False})
    print(f"Task '{task}' added successfully")

def mark_done(x):
    show_tasks(x)
    try:
        index = int(input("\nWhich number is done: ")) - 1
        task = x[index]
        task["done"] = not task["done"]
        print(f"Task '{task['name']}' marked as {'done ✅' if task['done'] else 'not done ❌'}")
    except (ValueError, IndexError):
        print("Invalid task number")

    

def delete_task(x):
    show_tasks(x)
    try:
        index = int(input("\nEnter task number to delete: ")) - 1
        removed = x.pop(index)
        print(f"Task '{removed['name']}' deleted")
    except (ValueError, IndexError):
        print("Invalid task number")

def main():
    print("\n📝 Welcome to Your To-Do List App!")
    
    tasks = []
    while True:
        show_menu()
        choice = input("\nEnter your choice: ")
        
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            if len(tasks) == 0:
                print("You need to add a task first!")
                continue
            else:
                mark_done(tasks)
        elif choice == "4":
            if len(tasks) == 0:
                print("You need to add a task first!")
                continue
            else:
                delete_task(tasks)
        elif choice == "5":
            print("\nThank you for your work!")
            break
        else:
            print("Please enter a valid number!")

if __name__ == "__main__":
    main()
