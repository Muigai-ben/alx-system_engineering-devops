#!/usr/bin/python3
"""script using this REST API, for a given employee ID,
returns information about his/her TODO list progress
import requests
from sys import argv


def fetch_employee_data(employee_id):
    """
    Fetch employee data from the given REST API.

    Args:
        employee_id (int): The employee ID.

    Returns:
        tuple: A tuple containing user data and TODO list data.
    """
    user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    todos_response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")

    user_data = user_response.json() if user_response.status_code == 200 else None
    todos_data = todos_response.json() if todos_response.status_code == 200 else None

    return user_data, todos_data


def calculate_todo_progress(todos_data):
    """
    Calculate TODO list progress.

    Args:
        todos_data (list): List of TODO items.

    Returns:
        tuple: A tuple containing the number of completed tasks and the total number of tasks.
    """
    total_tasks = len(todos_data) if todos_data else 0
    completed_tasks = sum(task['completed'] for task in todos_data) if todos_data else 0

    return completed_tasks, total_tasks


def display_todo_progress(user_data, completed_tasks, total_tasks, todos_data):
    """
    Display TODO list progress information on the standard output.

    Args:
        user_data (dict): User data.
        completed_tasks (int): Number of completed tasks.
        total_tasks (int): Total number of tasks.
        todos_data (list): List of TODO items.
    """
    if user_data:
        print(f"Employee {user_data['name']} is done with tasks ({completed_tasks}/{total_tasks}):")

        for task in todos_data:
            if task['completed']:
                print(f"\t{task['title']}")


if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: python script.py <employee_id>")
        exit(1)

    employee_id = int(argv[1])

    user_data, todos_data = fetch_employee_data(employee_id)
    completed_tasks, total_tasks = calculate_todo_progress(todos_data)
    display_todo_progress(user_data, completed_tasks, total_tasks, todos_data)
