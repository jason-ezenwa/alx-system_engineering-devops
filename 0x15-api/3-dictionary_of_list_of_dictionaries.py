#!/usr/bin/python3
"""A script that uses an API to return info for a specific employee"""

import json
import requests
import sys


def fetching_recur():
    for i in range(1, 11):
        employee_id = i
        fetching(employee_id)


def fetching(employee_id):
    todo_url = "https://jsonplaceholder.typicode.com/" \
               "todos?userId={}".format(employee_id)
    username_url = "https://jsonplaceholder.typicode.com/" \
                   "users/{}".format(employee_id)

    to_do_response = requests.get(todo_url)
    employee_response = requests.get(username_url)

    to_do_tasks = to_do_response.json()
    employee_data = employee_response.json()

    employee_name = employee_data["username"]

    json_data = {employee_id: []}
    for task in to_do_tasks:
        json_data[employee_id].append(
            {"task": task["title"], "completed": task["completed"], "username": employee_name})

    filename = "todo_all_employees.json"
    with open(filename, 'w') as jsonfile:
        json.dump(json_data, jsonfile)


if __name__ == "__main__":
    fetching_recur()
