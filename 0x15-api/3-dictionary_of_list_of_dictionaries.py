#!/usr/bin/python3
"""Dictionary of list of dictionaries
"""

import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    with open("todo_all_employees.json", "w") as json_file:
        all_users = {}
        for u_user in users:
            todos = requests.get(
                url + "todos", params={"userId": u_user["id"]}).json()
            all_tasks = []
            for task in todos:
                all_tasks.append({"username": u_user["name"],
                                  "task": task["title"],
                                  "completed": task["completed"]})
            all_users[u_user["id"]] = all_tasks
        json.dump(all_users, json_file)
