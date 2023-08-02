to_do_list = []

# Function to display the current to-do list
def display_list():
    if not to_do_list:
        print("Your to-do list is empty.")
    else:
        print("Your to-do list:")
        for index, task in enumerate(to_do_list, start=1):
            print(f"{index}. {task}")

# Function to add a new task to the to-do list
def add_task(task):
    to_do_list.append(task)
    print(f"Task '{task}' added to the to-do list.")

# Function to remove a task from the to-do list
def remove_task(index):
    if 1 <= index <= len(to_do_list):
        removed_task = to_do_list.pop(index - 1)
        print(f"Task '{removed_task}' removed from the to-do list.")
    else:
        print("Invalid task index.")

# Main loop
while True:
    print("\n--- To-Do List Manager ---")
    print("1. Display To-Do List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        display_list()
    elif choice == '2':
        new_task = input("Enter the new task: ")
        add_task(new_task)
    elif choice == '3':
        display_list()
        task_index = int(input("Enter the task index to remove: "))
        remove_task(task_index)
    elif choice == '4':
        print("Exiting To-Do List Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
