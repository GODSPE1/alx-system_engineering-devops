#!/usr/bin/python3
"""
Fetching data for a given employee ID, returns information about
his/her Todo list progress.
"""
import json
import requests
import sys


def main():
    """Function of the module that get the username, title and task"""
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        return

    employee_id = sys.argv[1]

    todos_response = requests.get(
        f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
    user_response = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}')

    todos = todos_response.json()
    user = user_response.json()

    user_tasks = {}
    for todo in todos:
        task_info = {
            'task': todo['title'],
            'completed': todo['completed'],
            'username': user['username']
        }
        user_tasks.setdefault(employee_id, []).append(task_info)

    json_data = json.dumps(user_tasks, indent=4)

    filename = f'{user["id"]}.json'

    with open(filename, 'w') as file:
        file.write(json_data)


if __name__ == "__main__":
    main()
