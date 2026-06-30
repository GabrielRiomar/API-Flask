from flask import Flask

# Initialize Flask app
app = Flask(__name__)

# Register blueprints
from routes.task import task_bp
app.register_blueprint(task_bp)

# Development server
if __name__ == "__main__":
  app.run(debug=True, port=5001)