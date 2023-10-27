#!/usr/bin/python
"""
Import requests module
"""
import requests
"""
Import sys module to get command line arguments
"""
import sys

"""
Get the employee ID from the first argument
"""
employee_id = sys.argv[1]

"""
Define the base URL for the API
"""
base_url = "https://jsonplaceholder.typicode.com/users/"

"""Get the employee details from the API"""
employee = requests.get(base_url + employee_id).json()

"""Get the employee name"""
employee_name = employee["name"]

""" Get the employee TODO list from the API"""
todos = requests.get(base_url + employee_id + "/todos").json()

"""Initialize the total and done tasks counters"""
total_tasks = 0
done_tasks = 0

"""Initialize an empty list for the done tasks titles"""
done_tasks_titles = []

"""Loop through the todos list and update the counters and titles list"""
for todo in todos:
    total_tasks += 1
    if todo["completed"]:
        done_tasks += 1
        done_tasks_titles.append(todo["title"])

"""Print the first line with the employee name and tasks progress"""
print("Employee {} is done with tasks({}/{}):".format(employee_name, done_tasks, total_tasks))


"""Print the titles of the done tasks with a tabulation and a space before each one"""
for title in done_tasks_titles:
    print("\t " + title)