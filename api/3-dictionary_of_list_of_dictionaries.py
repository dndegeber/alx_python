#!/usr/bin/python3
import requests
import json

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    users = response.json()

    tasks = {}
    for user in users:
        user_id = str(user["id"])
        username = user["username"]

        url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
        response = requests.get(url)
        todos = response.json()

        task_list = []
        for todo in todos:
            task_list.append({
                "username": username,
                "task": todo["title"],
                "completed": todo["completed"]
            })

        tasks[user_id] = task_list

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(tasks, json_file)
