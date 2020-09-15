#!/usr/bin/python3
"""Export to CSV
"""
import csv
import requests
from sys import argv
if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/" + argv[1]).json()
    u_name = user["username"]
    todos = requests.get(url + "todos", params={"userId": argv[1]}).json()
    u_id = user["id"]
    with open("{}.csv".format(u_id), "w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for tasks in todos:
            writer.writerow([u_id, u_name, tasks["completed"], tasks["title"]])
