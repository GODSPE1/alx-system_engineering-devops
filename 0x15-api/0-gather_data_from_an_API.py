#!/usr/bin/python3
"""
Fetching data for a given employee ID, returns information about
his/her TODO list progress.
"""
import json
import requests
import sys


def main():
    """de"""
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

    user_tasks = {}

    for todo in todos:
        user_tasks[todo['id']] = {
            'task': todo['title'],
            'completed': todo['completed']
        }

    num_completed_tasks = sum(1 for todo in todos if todo['completed'])
    total_tasks = len(todos)

    print(f"Employee {user['name']} is done with tasks "
          f"({num_completed_tasks}/{total_tasks}): ")
    for todo in todos:
        if todo['completed']:
            print(f"\t{todo['title']}")

    print(json.dumps(user_tasks, indent=4))


if __name__ == "__main__":
    main()
