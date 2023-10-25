#!/usr/bin/python3
"""
Fetches and exports information about a user's completed tasks.
"""

import csv
import requests
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

        completed_tasks = [(user_data.get('id'), user_data.get('username'), task.get('completed'), task.get('title')) for task in todo_data]

        # Save to CSV file
        file_name = f"{user_data.get('id')}.csv"
        with open(file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
            writer.writerows(completed_tasks)

        print(f"Data exported to {file_name}")
    else:
        print(f"Error fetching data for employee ID {employee_id}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_info(employee_id)
