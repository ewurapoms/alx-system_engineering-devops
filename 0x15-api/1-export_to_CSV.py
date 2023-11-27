#!/usr/bin/python3
"""Exports employee's ID data on todo list to CSV format"""

from requests import get
import sys
import csv


if __name__ == '__main__':
    user_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    data = get(url)
    username = data.json().get('username')

    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)
    data = get(url)
    todos = data.json()
    with open('{}.csv'.format(user_id), 'w') as file:
        for task in todos:
            file.write('"{}","{}","{}","{}"\n'
                       .format(user_id, username, task.get('completed'),
                               task.get('title')))
