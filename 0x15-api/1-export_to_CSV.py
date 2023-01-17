#!/usr/bin/python3
"""a script that uses an API to return info for a specific employee"""
import csv

import requests
import sys

if __name__ == '__main__':
    employee_id = sys.argv[1]  # take the input employee_id from command line
    todo_url = f"https://jsonplaceholder.typicode.com/" \
               f"todos?userId={employee_id}"
    username_url = f"https://jsonplaceholder.typicode.com/" \
                   f"users/{employee_id}"

    # send a GET request to todo_url and username_url
    # to retrieve the todo and employee data
    to_do_response = requests.get(todo_url)
    employee_response = requests.get(username_url)

    # retrieve the data in json format
    to_do_tasks = to_do_response.json()
    employee_data = employee_response.json()

    # get the name of the employee
    employee_name = employee_data["name"]
    information = []
    for task in to_do_tasks:
        information.append([employee_id, employee_name, task['completed'], task['title']])
    filename = employee_id + ".csv"
    with open(filename, "w", newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(information)