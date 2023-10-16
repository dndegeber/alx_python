#!/usr/bin/python3
"""
This script retrieves tasks for all users from a REST API and exports the data in JSON format.
"""

import json
import requests

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    users = response.json()

    tasks = {}
    for user in users:
        user_id = str(user.get("id"))
        username = user.get("username")

        url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
        response = requests.get(url)
        todos = response.json()

        task_list = []
        for todo in todos:
            task_list.append({
                "username": username,
                "task": todo.get("title"),
                "completed": todo.get("completed")
            })

        tasks[user_id] = task_list

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(tasks, json_file)
