#!/usr/bin/python3
"""
Returns to-do list information for a given employee ID.
"""


import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])

    user_info = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                             .format(employee_id)).json()
    if 'name' not in user_info:
        print("Employee with ID {} not found".format(employee_id))
        sys.exit(1)

    todo_list = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'
        .format(employee_id)).json()

    total_tasks = len(todo_list)
    completed_tasks = sum(1 for task in todo_list if task['completed'])

    print("Employee {} is done with tasks({}/{}):"
          .format(user_info['name'], completed_tasks, total_tasks))
    for task in todo_list:
        if task['completed']:
            print("\t{}".format(task['title']))
