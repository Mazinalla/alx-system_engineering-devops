#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys


def get_employee_info(emp_id):
    # URL to get employee information
    user_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    # URL to get employee's TODO list
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={emp_id}"

    # Get employee information
    user_response = requests.get(user_url)
    # Get employee's TODO list
    todos_response = requests.get(todos_url)

    if user_response.status_code == 200 and todos_response.status_code == 200:
        user_data = user_response.json()
        todos_data = todos_response.json()

        # Extract employee name
        emp_name = user_data['name'].strip()

        # Calculate total and completed tasks
        t_t = len(todos_data)
        completed_tasks = [task for task in todos_data if task['completed']]
        n_o_d_t = len(completed_tasks)

        # Print the TODO list progress
        print(f"Employee {emp_name} is done with tasks({n_o_d_t}/{t_t}):")

        # Print the titles of completed tasks
        for task in completed_tasks:
            print(f"\t {task['title']}")
    else:
        print("Failed to retrieve data. Check the employee ID and try again.")


if __name__ == "__main__":
    # Get the employee ID from command line arguments
    emp_id = int(sys.argv[1])

    # Get the employee's TODO list progress
    get_employee_info(emp_id)
