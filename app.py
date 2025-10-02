from flask import Flask, request, jsonify
from models.task import Task

# Initialize Flask app
app = Flask(__name__)

# In-memory storage for tasks
tasks = []

# Initialize a counter for task IDs
task_id_counter = 1

# Create a new task
@app.route('/tasks', methods=['POST'])
def create_task():
  global task_id_counter
  data = request.get_json()
  new_task = Task(id=task_id_counter, title=data['title'], description=data.get('description', ''), completed=False)
  task_id_counter += 1
  tasks.append(new_task)
  print(tasks)
  return {'id': new_task.id, 'title': new_task.title, 'description': new_task.description, 'completed': new_task.completed}, 201

# Retrieve all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
  task_list = [task.to_dict() for task in tasks]
  output = {'tasks': task_list,
            'total': len(task_list)}
  return jsonify(output), 200

# Retrieve a specific task by ID
@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
  for task in tasks:
    if task.id == id:
      return jsonify(task.to_dict()), 200
  return {'message': 'Task not found'}, 404

# Update a task by ID
@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
  data = request.get_json()
  for task in tasks:
    if task.id == id:
      task.title = data.get('title', task.title)
      task.description = data.get('description', task.description)
      task.completed = data.get('completed', task.completed)
      return jsonify(task.to_dict()), 200
  return {'message': 'Task not found'}, 404

# Delete a task by ID
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    for t, task in enumerate(tasks):
        if task.id == id:
            tasks.pop(t)
            return {'message': 'Task deleted successfully'}, 200
    return {'message': 'Task not found'}, 404

# Development server
if __name__ == "__main__":
  app.run(debug=True, port=5001)