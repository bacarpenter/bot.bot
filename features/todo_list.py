# Copyright (C) Ben Carpenter, 2021. Licensed under the MIT license.

from typing import Dict, List
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Init access to db
cred = credentials.Certificate("secrets/firebase-adminsdk.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


def db_add_todo(task: str) -> int:
    # Get next todo id
    next_id = int(db.collection('counter').document(
        'counter').get().to_dict()['counter']) + 1

    # Create a new todo entry
    todo_ref = db.collection('tasks').document(f"task#{next_id}")
    todo_ref.set({'task': task, 'done': False, 'id': next_id})

    # +1 to counter
    db.collection('counter').document('counter').set({'counter': next_id})

    return next_id


def db_read_todo(id: int) -> Dict:
    todo_ref = db.collection('tasks').document(f"task#{id}").get().to_dict()
    return todo_ref


def db_read_all() -> List:
    todos_ref = db.collection('tasks').stream()
    todos = []
    for todo in todos_ref:
        todos.append(todo.to_dict())

    return todos


def db_complete(id: int) -> None:
    todo_ref = db.collection('tasks').document(f"task#{id}")
    todo_ref.set({'done': True, }, merge=True)

# Conversational responces


def new_task(message: str, settings) -> List:
    rList = []
    id = db_add_todo(message[message.index(":") + 2:])
    rList.append(
        f"Copy that! I'll add this to your to do list, {settings['user_name']}!")
    task = db_read_todo(id)
    rList.append(
        f"Task #{task['id']}: {task['task']}\tStatus: {'done' if task['done'] else 'todo' }")
    return rList


def read(message: str, settings) -> List:
    rList = []
    tasks = db_read_all()
    rList.append(f"Here's you're todos:")
    for task in tasks:
        rList.append(
            f"Task #{task['id']}: {task['task']}\tStatus: {'done' if task['done'] else 'todo' }")

    return rList


def complete(message: str, settings) -> List:
    db_complete(int(message[message.index(":") + 2:]))
    task = db_read_todo(int(message[message.index(":") + 2:]))
    return ["Got it!", f"Task #{task['id']}: {task['task']}\tStatus: {'done' if task['done'] else 'todo' }"]
