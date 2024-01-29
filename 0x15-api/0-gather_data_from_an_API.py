#!/usr/bin/python3
"Display Employee tasks"
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
    done_todos = [todo for todo in todos if todo.get("completed") is True]

    print((f"Employee {user.get('name')} is done with tasks("
           f"{len(done_todos)}/{len(todos)}):"))
    for item in done_todos:
        print("\t ", item.get("title"))


if __name__ == "__main__":
    fetch()
