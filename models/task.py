class Task:
  # Constructor to initialize a Task object
  def __init__(self, id, title, description, completed=False):
    self.id = id
    self.title = title
    self.description = description
    self.completed = completed

# Method to convert Task object to dictionary
  def to_dict(self):
    return{
      "id": self.id,
      "title": self.title,
      "description": self.description,
      "completed": self.completed
    }