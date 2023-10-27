#!/usr/bin/python
"""
Import requests module
"""
import requests
"""
Import sys module to get command line arguments
"""
import sys
import csv

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

"""Initialize an empty list to store task records"""
task_records = []

"""Loop through the todos list and update the task records list"""
for todo in todos:
    task_record = [employee_id, employee_name, str(todo["completed"]), todo["title"]]
    task_records.append(task_record)

"""Write task records to CSV file"""
csv_file_name = "{}.csv".format(employee_id)
with open(csv_file_name, mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerows(task_records)

print(f"Data exported to {csv_file_name}")
