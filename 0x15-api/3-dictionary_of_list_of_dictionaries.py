#!/usr/bin/python3
"Save all employees with their tasks to a JSON file"
import json
import requests


def fetch():
    TODOS_URL = "https://jsonplaceholder.typicode.com/todos"
    USERS_URL = "https://jsonplaceholder.typicode.com/users"

    res = requests.get(f"{USERS_URL}")
    users = res.json()

    data = {}
    for user in users:
        res = requests.get(TODOS_URL, params={"userId": user.get('id')})
        todos = res.json()
        tasks = []
        for todo in todos:
            tasks.append({
                'username': user.get('username'),
                'task': todo.get('title'),
                'completed': todo.get('completed')
            })
        data[user.get('id')] = tasks

    with open('todo_all_employees.json', 'w') as f:
        json.dump(data, f)


if __name__ == "__main__":
    fetch()
