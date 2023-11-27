#!/usr/bin/python3
"""Exports employee data to JSON format"""
import json
import requests
import sys


def todo_json():
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    task_list = {}

    for user in users:
        user_id = user['id']
        username = user['username']

        todos = requests.get(url + "todos", params={"userId": user_id}).json()
        user_tasks = [
            {
                "username": username,
                "task": task["title"],
                "completed": task["completed"]
            }
            for task in todos
        ]
        task_list[user_id] = user_tasks

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(task_list, json_file, indent=2)


if __name__ == "__main__":
    todo_json()
