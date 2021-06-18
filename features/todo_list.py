# Copyright (C) Ben Carpenter, 2021. Licensed under the MIT license.

from typing import Dict, List
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Init access to db
cred = credentials.Certificate("secrets/firebase-adminsdk.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# Change to change format. Keep id, task, and status
todo_template = "**Task {id}:** {task} | *Status: {status}*"

# Data base functions


def db_add_todo(task: str) -> int:
    """Add an entry to the db"""
    # Get next todo id
    next_id = int(db.collection('counter').document(
        'counter').get().to_dict()['counter']) + 1

    # Create a new todo entry
    todo_ref = db.collection('tasks').document(f"task#{next_id}")
    todo_ref.set({'task': task,
                  'done': False,
                  'id': next_id,
                  'time_stamp': firestore.SERVER_TIMESTAMP})

    # +1 to counter
    db.collection('counter').document('counter').set({'counter': next_id})

    return next_id


def db_read_todo(id: int) -> Dict:
    """Read the document with given ID from the database. Return it as a dict"""
    todo_ref = db.collection('tasks').document(f"task#{id}").get().to_dict()
    return todo_ref


def db_read_all() -> List:
    """Read all documents from the db. Return as a list of dicts"""
    todos_ref = db.collection('tasks').stream()
    todos = []
    for todo in todos_ref:
        todos.append(todo.to_dict())

    todos.sort(key=lambda i: i['time_stamp'])
    return todos


def db_complete(id: int) -> None:
    """Mark the entry with given id as complete."""
    todo_ref = db.collection('tasks').document(f"task#{id}")
    todo_ref.set({'done': True, }, merge=True)


def db_delete(id: int) -> None:
    """Delete document of given id from DB"""
    db.collection('tasks').document(f"task#{id}").delete()


def db_counter_decrement() -> None:
    """Decrement counter for use by testing"""
    db.collection('counter').document('counter').set({'counter': int(db.collection('counter').document(
        'counter').get().to_dict()['counter']) - 1})


def db_clear_list() -> None:
    docs = db.collection('tasks').stream()

    # From firebase SDK, https://firebase.google.com/docs/firestore/manage-data/delete-data#python
    for doc in docs:
        print(f'Deleting doc {doc.id} => {doc.to_dict()}')
        doc.reference.delete()

    db.collection('counter').document('counter').set({'counter': 0})

# Bot responce functions


def new_task(message: str, settings) -> List:
    rList = []
    id = db_add_todo(message[message.index(":") + 2:])
    rList.append(
        f"Copy that! I'll add this to your to do list, {settings['user_name']}!")
    task = db_read_todo(id)
    # rList.append(
    #     f"Task #{task['id']}: {task['task']}\tStatus: {'done' if task['done'] else 'todo' }")
    rList.append(todo_template.format(
        id=id, task=task['task'], status='done' if task['done'] else 'todo'))
    return rList


def read(message: str, settings) -> List:
    rList = []
    tasks = db_read_all()
    rList.append(f"Here's you're todos:")
    for task in tasks:
        rList.append(todo_template.format(
            id=task['id'], task=task['task'], status='done' if task['done'] else 'todo'))

    return rList


def complete(message: str, settings) -> List:
    db_complete(int(message[message.index(":") + 2:]))
    task = db_read_todo(int(message[message.index(":") + 2:]))
    return ["Got it!", todo_template.format(
            id=task['id'], task=task['task'], status='done' if task['done'] else 'todo')]


def delete(message: str, settings) -> List:
    db_delete(int(message[message.index(":") + 2:]))
    return [f"Done. Task {int(message[message.index(':') + 2:])} was deleted"]


def clear_list(message: str, settings) -> List:
    db_clear_list()
    return[f"Done! {settings['user_name']}, your todo list has been cleared"]
