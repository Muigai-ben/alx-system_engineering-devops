#!/usr/bin/python3
"""script using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""
import requests
from sys import argv

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: python script.py <employee_id>")
        exit(1)

    employee_id = int(argv[1])

    # Fetch user data
    user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    todos_response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")

    if user_response.status_code != 200 or todos_response.status_code != 200:
        print(f"Failed to fetch data. Check if the employee ID is valid.")
        exit(1)

    user_data = user_response.json()
    todos_data = todos_response.json()

    # Calculate TODO list progress
    total_tasks = len(todos_data)
    completed_tasks = sum(task['completed'] for task in todos_data)

    # Display information
    print(f"Employee {user_data['name']} is done with tasks ({completed_tasks}/{total_tasks}):")

    for task in todos_data:
        if task['completed']:
            print(f"\t{task['title']}")

