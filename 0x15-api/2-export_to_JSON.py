#!/usr/bin/python3

"""
extend my Python script to export data in the JSON format.
"""

import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <USER_ID>")
        sys.exit(1)

    user_id = sys.argv[1]

    # Fetch user data
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"User with ID {user_id} not found.")
        sys.exit(1)
    user = user_response.json()
    username = user.get("username")

    # Fetch tasks for the user
    tasks_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    tasks_response = requests.get(tasks_url)
    tasks = tasks_response.json()

    # Prepare JSON data
    tasks_list = []
    for task in tasks:
        tasks_list.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    json_data = {user_id: tasks_list}

    # Write to JSON file
    json_filename = f"{user_id}.json"
    with open(json_filename, mode='w', encoding='utf-8') as jsonfile:
        json.dump(json_data, jsonfile, indent=4)

    print(f"Data exported to {json_filename}")
