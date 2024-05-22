#!/usr/bin/python3

import requests
import sys

if __name__ == "__main__":
    # Base URL for the JSONPlaceholder API
    base_url = "https://jsonplaceholder.typicode.com/"

    # Get the employee ID from the command-line argument
    employee_id = sys.argv[1]

    # Get the employee information using the provided employee ID
    employee_info = requests.get(base_url + "users/{}".format(employee_id)).json()

    # Get the to-do list for the employee using the provided employee ID
    params = {"userId": employee_id}
    tasks = requests.get(base_url + "todos", params).json()

    # Filter completed tasks and count them
    completed_tasks = [task for task in tasks if task.get("completed") is True]

    # Print the employee's TODO list progress
    print("Employee {} is done with tasks({}/{}):".format(
        employee_info.get("name"),
        len(completed_tasks),
        len(tasks)
    ))

    # Print the completed tasks
    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
