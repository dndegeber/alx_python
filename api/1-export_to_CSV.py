import requests
import sys
import csv

def get_employee_info(employee_id):
    user_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    todo_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')

    if user_response.status_code == 200 and todo_response.status_code == 200:
        user_data = user_response.json()
        todo_data = todo_response.json()

        completed_tasks = [task for task in todo_data if task.get('completed')]

        print(f"Employee {user_data.get('name')} is done with tasks({len(completed_tasks)}/{len(todo_data)}):")
        for task in completed_tasks:
            print(f"\t{task.get('title')}")

        # Export to CSV
        csv_filename = f"{user_data.get('id')}.csv"
        with open(csv_filename, mode='w', newline='') as csv_file:
            fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            for task in todo_data:
                writer.writerow({
                    'USER_ID': user_data.get('id'),
                    'USERNAME': user_data.get('username'),
                    'TASK_COMPLETED_STATUS': task.get('completed'),
                    'TASK_TITLE': task.get('title')
                })
        print(f"Data exported to {csv_filename}")
    else:
        print(f"Error fetching data for employee ID {employee_id}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)
    employee_id = int(sys.argv[1])
    get_employee_info(employee_id)
