#!/usr/bin/python3
"Save tasks to a JSON file"
import json
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

    data = []
    for todo in todos:
        data.append({
            'task': todo.get('title'),
            'completed': todo.get('completed'),
            'username': user.get('username')})

    with open(f'{user_id}.json', 'w') as f:
        json.dump({f'{user_id}': data}, f)


if __name__ == "__main__":
    fetch()
