#!/usr/bin/env python3
"""
Script to fetch and export employee TODO list progress to a JSON file.
"""

import requests
import json
import sys

def get_employee_info(employee_id):
    """
    Fetches and prints information about a user's completed tasks.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    user_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    todo_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')

    if user_response.status_code == 200 and todo_response.status_code == 200:
        user_data = user_response.json()
        todo_data = todo_response.json()

        completed_tasks = [{"task": task.get('title'), "completed": task.get('completed'), "username": user_data.get('username')} for task in todo_data]

        json_data = {str(user_data.get('id')): completed_tasks}

        print(f"Employee {user_data.get('name')} is done with tasks({len(completed_tasks)}/{len(todo_data)}):")
        for task in completed_tasks:
            print(f"\t{task['task']}")

        # Export to JSON
        json_filename = f"{user_data.get('id')}.json"
        with open(json_filename, mode='w') as json_file:
            json.dump(json_data, json_file)
        print(f"Data exported to {json_filename}")
    else:
        print(f"Error fetching data for employee ID {employee_id}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)
    employee_id = int(sys.argv[1])
    get_employee_info(employee_id)
