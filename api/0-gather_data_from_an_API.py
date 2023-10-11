import requests
import sys

def get_employee_info(employee_id):
    # Define the API endpoints
    user_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    todo_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')

     # Fetch employee information
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Fetch employee's TODO list
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Calculate the number of completed and total tasks
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo['completed'])

    # Print the employee's TODO list progress in the specified format
    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
    for index, todo in enumerate(todos_data, start=1):
        if todo['completed']:
            print(f"\t{todo['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_info(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)
