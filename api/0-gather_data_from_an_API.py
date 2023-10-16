#!/usr/bin/python3
"""
Fetches employee info from REST API
"""

import requests
import sys

users_url = "https://jsonplaceholder.typicode.com/users"
todos_url = "https://jsonplaceholder.typicode.com/todos"


def get_employee_info(employee_id):
    """ Fetch employee name, number of tasks """

    user_data = requests.get(f"{users_url}/{employee_id}").json()
    employee_name = user_data['name']

    todo_data = requests.get(f"{users_url}/{employee_id}/todos").json()
    num_completed_tasks = len([task for task in todo_data if task['completed']])
    total_tasks = len(todo_data)

    print(f"Employee {employee_name} is done with tasks({num_completed_tasks}/{total_tasks}):")
    for task in [task for task in todo_data if task['completed']]:
        print(f"\t{task['title']}")


if __name__ == "__main__":
    def check_tasks(id):
        """ Check student output for formatting """

        filename = 'student_output'
        count = 0
        with open(filename, 'r') as f:
            next(f)
            for line in f:
                count += 1
                if line[0] == '\t' and line[1] == ' ' and line[-1] == '\n':
                    print("Task {} Formatting: OK".format(count))
                else:
                    print("Task {} Formatting: Incorrect".format(count))

    check_tasks(int(sys.argv[1]))

