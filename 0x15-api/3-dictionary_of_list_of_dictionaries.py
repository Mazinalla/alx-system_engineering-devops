#!/usr/bin/python3

"""
extend my Python script to export data in the JSON format.
"""

import json
import requests

if __name__ == "__main__":
    # Fetch all users
    users_url = "https://jsonplaceholder.typicode.com/users"
    users_response = requests.get(users_url)
    users = users_response.json()

    # Prepare the final JSON data
    all_tasks = {}

    for user in users:
        user_id = str(user.get("id"))
        username = user.get("username")

        # Fetch tasks for the current user
        t_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
        tasks_response = requests.get(t_url)
        tasks = tasks_response.json()

        # Prepare the list of tasks for this user
        tasks_list = []
        for task in tasks:
            tasks_list.append({
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            })

        # Add this user's tasks to the final dictionary
        all_tasks[user_id] = tasks_list

    # Write the final JSON data to a file
    json_filename = "todo_all_employees.json"
    with open(json_filename, mode='w', encoding='utf-8') as jsonfile:
        json.dump(all_tasks, jsonfile, indent=4)

    print(f"Data exported to {json_filename}")
