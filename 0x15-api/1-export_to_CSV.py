#!/usr/bin/python3
"""A script that uses an API to return info for a specific employee"""
import csv
import requests
import sys

if __name__ == '__main__':
    employee_id = sys.argv[1]  # take the input employee_id from command line
    todo_url = "https://jsonplaceholder.typicode.com/" \
               "todos?userId={}".format(employee_id)
    username_url = "https://jsonplaceholder.typicode.com/" \
                   "users/{}".format(employee_id)

    # send a GET request to todo_url and username_url
    # to retrieve the todo and employee data
    to_do_response = requests.get(todo_url)
    employee_response = requests.get(username_url)

    # retrieve the data in json format
    to_do_tasks = to_do_response.json()
    employee_data = employee_response.json()

    # get the name of the employee
    employee_name = employee_data["username"]
    information = []
    for task in to_do_tasks:
        information.append([employee_id,
                            employee_name, task['completed'], task['title']])
    filename = employee_id + ".csv"
    with open(filename, "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        csvwriter.writerows(information)
