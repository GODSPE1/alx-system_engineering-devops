#!/usr/bin/python3
"""
Fetching data for a given employee ID, returns information about
his/her TODO list progress.
"""
import csv
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

    num_completed_tasks = sum(1 for todo in todos if todo['completed'])
    total_tasks = len(todos)

    print(f"Employee {user['name']} is done with tasks "
          f"({num_completed_tasks}/{total_tasks}): ")
    for todo in todos:
        if todo['completed']:
            print(f"\t{todo['title']}")

    filename = f'{user["id"]}.csv'

    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                         "TASK_TITLE"])

        for todo in todos:
            writer.writerow([user["id"], user["username"],
                             todo["completed"], todo["title"]])

    print(f"Data exported to {filename} successfully!")


if __name__ == "__main__":
    main()
