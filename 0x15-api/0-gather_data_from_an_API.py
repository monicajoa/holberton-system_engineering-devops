#!/usr/bin/python3
"""Gather data from an API
"""

import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/" + argv[1]).json()
    todos = requests.get(url + "todos", params={"userId": argv[1]}).json()
    completed_tasks = []
    for task in todos:
        if task["completed"] is True:
            completed_tasks.append(task["title"])
    print("Employee {} is done with tasks({}/{}):".format(
        user["name"], len(completed_tasks), len(todos)))
    for c_task in completed_tasks:
        print("\t {}".format(c_task))
