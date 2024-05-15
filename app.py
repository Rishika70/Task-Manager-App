# Define a class to represent a task
class Task:
  def __init__(self, description, urgency, department):
    self.description = description
    self.urgency = urgency
    self.department = department
    self.status = "pending"  # Default status

  def update_status(self, new_status):
    self.status = new_status

  def transfer_department(self, new_department):
    self.department = new_department


# Function to create a new task
def create_task():
  description = input("Enter task description: ")
  urgency = input("Enter urgency (high/medium/low): ")
  department = input("Enter assigned department: ")
  return Task(description, urgency, department)


# Function to view tasks for a specific department
def view_department_tasks(department):
  # Simulate fetching tasks from a database (replace with actual data retrieval)
  tasks = [
      Task("Write report", "high", department),
      Task("Update website", "medium", department),
  ]
  print(f"\nTasks for department: {department}")
  for task in tasks:
    print(f"\tDescription: {task.description}")
    print(f"\tUrgency: {task.urgency}")
    print(f"\tStatus: {task.status}")
    print("-" * 20)


# Function to update task status
def update_task_status(tasks):
  # Simulate fetching tasks from a database (replace with actual data retrieval)
  all_tasks = tasks  # Replace with actual list of tasks
  print("\nList of all tasks:")
  for i, task in enumerate(all_tasks):
    print(f"\t{i+1}. {task.description} ({task.department}) - {task.status}")
  task_choice = int(input("Enter the number of the task to update: ")) - 1
  if 0 <= task_choice < len(all_tasks):
    new_status = input("Enter new status (completed/pending/transferred): ")
    all_tasks[task_choice].update_status(new_status)
    print("Task status updated successfully!")
  else:
    print("Invalid task choice!")


# Function to transfer tasks to another department
def transfer_task(tasks):
  # Simulate fetching tasks from a database (replace with actual data retrieval)
  all_tasks = tasks  # Replace with actual list of tasks
  print("\nList of all tasks:")
  for i, task in enumerate(all_tasks):
    print(f"\t{i+1}. {task.description} ({task.department}) - {task.status}")
  task_choice = int(input("Enter the number of the task to transfer: ")) - 1
  if 0 <= task_choice < len(all_tasks):
    new_department = input("Enter the department to transfer to: ")
    all_tasks[task_choice].transfer_department(new_department)
    print("Task transferred successfully!")
  else:
    print("Invalid task choice!")


# Main loop for user interaction
tasks = []  # Replace with actual data storage (e.g., database)
while True:
  print("\nTask Management System")
  print("1. Create Task")
  print("2. View Department Tasks")
  print("3. Update Task Status")
  print("4. Transfer Task")
  print("5. Exit")
  choice = input("Enter your choice: ")

  if choice == "1":
    new_task = create_task()
    tasks.append(new_task)
    print("Task created successfully!")
  elif choice == "2":
    department = input("Enter department name: ")
    view_department_tasks(department)
  elif choice == "3":
    update_task_status(tasks)
  elif choice == "4":
    transfer_task(tasks)
  elif choice == "5":
    print("Exiting...")
    break
  else:
    print("Invalid choice!")
