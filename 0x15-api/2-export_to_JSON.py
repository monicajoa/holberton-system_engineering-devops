#!/usr/bin/python3
"""Export to JSON
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/" + argv[1]).json()
    u_name = user["username"]
    todos = requests.get(url + "todos", params={"userId": argv[1]}).json()
    u_id = user["id"]
    with open("{}.json".format(u_id), "w") as json_file:
        info = {u_id: []}
        for task in todos:
            info[u_id].append(
                {
                    "task": task["title"],
                    "completed": task["completed"],
                    "username": u_name
                }
            )
        json.dump(info, json_file)
