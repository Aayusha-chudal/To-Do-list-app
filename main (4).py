# makeing the empty list of the tasks
tasks = []


#  to add the tasks
def add_task(task):
  tasks.append(task)
  print("Task added: " + task)


# to view all the task in the list
def view_tasks():
  if not tasks:
    print("No tasks in the list.")
  else:
    print("Tasks:")
    for i, task in enumerate(tasks, 1):
      print(f"{i}. {task}")


# Function to mark a task as completed
def complete_task(task_index):
  if 1 <= task_index <= len(tasks):
    task = tasks[task_index - 1]
    print(f"Completed task: {task}")
    tasks.pop(task_index - 1)
  else:
    print("Invalid task index.")


while True:
  print("\nOptions:")
  print("1. Add task")
  print("2. View tasks")
  print("3. Complete task")
  print("4. Quit")

  choice = input("Enter your choice (1/2/3/4): ")

  if choice == "1":
    task = input("Enter a task: ")
    add_task(task)
  elif choice == "2":
    view_tasks()
  elif choice == "3":
    task_index = int(input("Enter the task number to complete: "))
    complete_task(task_index)
  elif choice == "4":
    print("Thanks for using!")
    break
  else:
    print("Invalid choice. Please try again.")
