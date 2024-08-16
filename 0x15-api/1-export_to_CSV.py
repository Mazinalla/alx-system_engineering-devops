#!/usr/bin/python3

"""
extend my previous Python script to export data in the CSV format.
"""

import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <USER_ID>")
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

    print(f"Number of tasks fetched: {len(tasks)}")

    # Prepare CSV data
    csv_data = []
    for task in tasks:
        csv_data.append([
            user_id,
            username,
            task.get("completed"),
            task.get("title")
        ])

    # Debugging: Print tasks before writing to CSV
    for task in csv_data:
        print(task)

    # Write to CSV file
    csv_filename = f"{user_id}.csv"
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        csvwriter.writerows(csv_data)

    print(f"Data exported to {csv_filename}")
