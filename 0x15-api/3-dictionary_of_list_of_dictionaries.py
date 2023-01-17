#!/usr/bin/python3
"""Exports to-do list information of all employees to JSON format."""
import json
import requests

def fetch_all_employees_tasks():
    all_employees_tasks = {}

    for i in range(1, 11):
        employee_id = i
        employee_tasks = fetch_employee_tasks(employee_id)

        all_employees_tasks[employee_id] = employee_tasks

    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(all_employees_tasks, jsonfile)

def fetch_employee_tasks(employee_id):
    todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)
    username_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)

    to_do_response = requests.get(todo_url)
    employee_response = requests.get(username_url)

    to_do_tasks = to_do_response.json()
    employee_data = employee_response.json()

    employee_name = employee_data["username"]

    employee_tasks = []
    for task in to_do_tasks:
        task_data = {
            "username": employee_name,
            "task": task["title"],
            "completed": task["completed"]
        }
        employee_tasks.append(task_data)

    return employee_tasks

if __name__ == "__main__":
    fetch_all_employees_tasks()
