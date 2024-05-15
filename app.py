from flask import Flask, render_template, request

app = Flask(__name__)

# Define a class to represent a task
class Task:
  def __init__(self, description, urgency, department, status):
    self.description = description
    self.urgency = urgency
    self.department = department
    self.status = status

  def update_status(self, new_status):
    self.status = new_status

  def transfer_department(self, new_department):
    self.department = new_department

# Sample tasks (replace with database integration later)
tasks = [
    Task("Fix printer issue", "High", "IT", "pending"),
    Task("Review marketing proposal", "Medium", "Marketing", "pending")
]


@app.route("/")
def index():
  return render_template("index.html", tasks=tasks)


@app.route("/create_task", methods=["GET", "POST"])
def create_task():
  if request.method == "POST":
    description = request.form["description"]
    urgency = request.form["urgency"]
    department = request.form["department"]
    new_task = Task(description, urgency, department, "pending")
    tasks.append(new_task)
    return render_template("index.html", tasks=tasks, message="Task created successfully!")
  else:
    # Display the create task form
    return render_template("create_task.html")


# Implement routes for other functionalities like view department tasks, update status, transfer task (exercise for you)

if __name__ == "__main__":
  app.run(debug=True)
