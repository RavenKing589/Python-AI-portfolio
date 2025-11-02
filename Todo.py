# todo.py
import os

TODO_FILE = "tasks.txt"

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            return f.read().splitlines()
    return []

def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        f.write("\n".join(tasks))

def show_tasks(tasks):
    if not tasks:
        print("No tasks!")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def main():
    tasks = load_tasks()
    print("TO-DO LIST APP")
    
    while True:
        print("\n" + "="*20)
        show_tasks(tasks)
        print("\n[a]dd, [d]elete, [q]uit")
        choice = input("> ").lower()
        
        if choice == 'a':
            task = input("New task: ")
            tasks.append(task)
            save_tasks(tasks)
        elif choice == 'd':
            show_tasks(tasks)
            idx = int(input("Delete #: ")) - 1
            if 0 <= idx < len(tasks):
                tasks.pop(idx)
                save_tasks(tasks)
        elif choice == 'q':
            print("Saved! Bye!")
            break

if __name__ == "__main__":
    main()