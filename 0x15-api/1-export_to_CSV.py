#!/usr/bin/python3
"Save tasks to a CSV file"
import csv
import requests
from sys import argv


def fetch():
    TODOS_URL = "https://jsonplaceholder.typicode.com/todos"
    USERS_URL = "https://jsonplaceholder.typicode.com/users"

    user_id = argv[1]

    res = requests.get(f"{USERS_URL}/{user_id}")
    user = res.json()

    res = requests.get(TODOS_URL, params={"userId": user_id})
    todos = res.json()

    with open(f'{user_id}.csv', 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([user_id, user.get('username'),
                             todo.get('completed'), todo.get('title')])


if __name__ == "__main__":
    fetch()
