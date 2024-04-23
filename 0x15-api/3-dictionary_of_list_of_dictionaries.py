#!/usr/bin/python3
"""
Fetching data for a given employee ID, returns information about
his/her TODO list progress and exports data in JSON format.
"""
import json
import requests
import sys


def main():
    """Function to retrieve and export TODO list data"""
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        return

    # Getting the employee ID from the command-line argument
    employee_id = sys.argv[1]

    todos_response = requests.get(
        f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
    user_response = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}')

    todos = todos_response.json()
    user = user_response.json()

    user_tasks = []

    for todo in todos:
        user_tasks.append({
            'username': user['username'],
            'task': todo['title'],
            'completed': todo['completed']
        })

    # Create a dictionary with the user ID as the key
    user_data = {user['id']: user_tasks}

    # Export data to a JSON file
    filename = f'todo_all_employees.json'
    with open(filename, 'w') as json_file:
        json.dump(user_data, json_file, indent=4)


if __name__ == "__main__":
    main()
