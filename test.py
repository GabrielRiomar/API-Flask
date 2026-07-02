import pytest
import requests

#CRUD
BASE_URL = "http://127.0.0.1:5001"
tasks = []

def test_create_task():
    url = f"{BASE_URL}/tasks"
    payload = {
        "title": "Test Task",
        "description": "This is a test task"
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data['title'] == payload['title']
    assert data['description'] == payload['description']
    assert data['completed'] is False
    tasks.append(data['id'])  # Store the created task ID for later tests

def test_get_tasks():
    url = f"{BASE_URL}/tasks"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert 'tasks' in data
    assert 'total' in data

def test_get_task():
    if tasks:
        task_id = tasks[0]
        url = f"{BASE_URL}/tasks/{task_id}"
        response = requests.get(url)
        data = response.json()
        assert response.status_code == 200
        assert data['id'] == task_id
    else:
        pytest.skip("No tasks available to test get_task")

def test_update_task():
    if tasks:
        task_id = tasks[0]
        url = f"{BASE_URL}/tasks/{task_id}"
        payload = {
            "title": "Updated Test Task",
            "description": "This is an updated test task",
            "completed": True
        }
        response = requests.put(url, json=payload)
        assert response.status_code == 200
        data = response.json()
        assert data['title'] == payload['title']
        assert data['description'] == payload['description']
        assert data['completed'] == payload['completed']
        
        # Verify the update by fetching the task again
        response = requests.get(url)
        data = response.json()
        assert response.status_code == 200
        assert data['title'] == payload['title']
        assert data['description'] == payload['description']
        assert data['completed'] == payload['completed']
    else:
        pytest.skip("No tasks available to test update_task")

def test_delete_task():
    if tasks:
        task_id = tasks[0]
        url = f"{BASE_URL}/tasks/{task_id}"
        response = requests.delete(url)
        assert response.status_code == 200
        data = response.json()
        assert data['message'] == 'Task deleted successfully'
        
        # Verify the deletion by attempting to fetch the task again
        response = requests.get(url)
        assert response.status_code == 404
        data = response.json()
        assert data['message'] == 'Task not found'
        
        tasks.remove(task_id)  # Remove the deleted task ID from the list
    else:
        pytest.skip("No tasks available to test delete_task")