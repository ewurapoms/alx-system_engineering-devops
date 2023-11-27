#!/usr/bin/python3
"""Exports employee's ID data on todo list to JSON format"""

from sys import argv
import json
import requests


if __name__ == "__main__":
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
                "task": tasks.get("title"),
                "completed": tasks.get("completed"),
                "username": username
            } for tasks in todos]}, jsonfile)
