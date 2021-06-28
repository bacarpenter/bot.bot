# Copyright (C) Ben Carpenter, 2021

import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

db = None


def init_db():
   # Init DB
    global db
    if os.environ.get("CI") == "true":
        # Should only be run if project is on a CI server. Namely, GitHub actions

        # From https://www.w3schools.com/python/python_json.asp! Thanks W3
        cred_dict = json.loads(os.environ.get("FIREBASE_ADMINSDK"))

        cred = credentials.Certificate(cred_dict)
        firebase_admin.initialize_app(cred)
        db = firestore.client()
    else:
        # Should be run when most people use the service
        try:
            cred = credentials.Certificate("secrets/firebase-adminsdk.json")
            firebase_admin.initialize_app(cred)
            db = firestore.client()
        except FileNotFoundError:
            print("Setup needed")


# List of todo's. Updated by db_read_all()
todos = []

# Data base functions
# All database functions work with UNIQUE_IDs, not LOCAL_IDs


def db_add_todo(todo):
    """Add the given todo as a record in the database"""
    if not db:
        init_db()
    # Get next todo id
    next_id = int(db.collection('counter').document(
        'counter').get().to_dict()['counter']) + 1

    # Create a new todo entry
    todo_ref = db.collection('tasks').document(f"task #{next_id}")
    todo_ref.set({'task': todo,
                  'done': False,
                  'unique_id': next_id,
                  'time_stamp': firestore.SERVER_TIMESTAMP})

    # +1 to counter
    db.collection('counter').document('counter').set({'counter': next_id})


def db_read_all():
    """Set todos to a list of dictionaries, sorted by date-time created, from the database"""

    if not db:
        init_db()
    global todos  # Allow me to edit todos directly
    todos = []  # Wipe todos blank

    todos_ref = db.collection('tasks').stream()
    for todo in todos_ref:
        todos.append(todo.to_dict())

    todos.sort(key=lambda i: i['time_stamp'])  # Sort by date-time
    # NOTE: Because of this sort, local_id's are just the index of the todo in the list, -1 because todos are 1 indexed. However, to deal with formatting, I will also include a key in the dictionary
    i = 1
    for todo in todos:
        todo['local_id'] = i
        i += 1


def db_complete(unique_id):
    """Mark task with id of `unique_id` as done."""
    if not db:
        init_db()
    todo_ref = db.collection('tasks').document(f"task #{unique_id}")
    todo_ref.set({'done': True, }, merge=True)


def db_delete(unique_id):
    """Delete record with unique id of `unique_id`"""
    if not db:
        init_db()
    db.collection('tasks').document(f"task #{unique_id}").delete()


def db_clear_all():
    """Deletes all todo records in the data base, leaving you with a blank slate."""
    if not db:
        init_db()
    docs = db.collection('tasks').stream()

    # From firebase SDK, https://firebase.google.com/docs/firestore/manage-data/delete-data#python
    for doc in docs:
        doc.reference.delete()

    db.collection('counter').document('counter').set({'counter': 0})


def db_counter_decrement():
    """Decrement counter for use by testing"""
    if not db:
        init_db()
    db.collection('counter').document('counter').set({'counter': int(db.collection('counter').document(
        'counter').get().to_dict()['counter']) - 1})


# Bot response functions
# All bot functions work with LOCAL_IDs, not UNIQUE_IDs


todo_str = "**Task {id}:** {task} | *Status: {status}*"


def new_todo(message, settings):
    """Add a new todo and respond with a conformation"""
    rList = []
    db_add_todo(message[message.index(":") + 2:])
    db_read_all()
    task = todos[-1]
    rList.append(
        f"Copy that! I'll add this to your to do list, {settings['user_name']}!")
    rList.append(todo_str.format(
        id=task['local_id'], task=task['task'], status='done' if task['done'] else 'todo'))

    return rList


def read_all(message, settings):
    """Return all todos formatted in markdown."""
    rList = []
    db_read_all()
    rList.append(f"Here's you're todos:")
    for task in todos:
        rList.append(todo_str.format(
            id=task['local_id'], task=task['task'], status='done' if task['done'] else 'todo'))

    return rList


def complete(message, settings):
    """Mark a todo as tone, and respond with conformation"""
    local_id = int(message[message.index(":") + 2:])
    db_complete(local_to_unique(local_id))
    db_read_all()
    task = todos[local_id - 1]
    return ["Got it!", todo_str.format(
            id=task['local_id'], task=task['task'], status='done' if task['done'] else 'todo')]


def delete(message, settings):
    """Delete a todo from the data base and respond with a conformation"""
    local_id = int(message[message.index(":") + 2:])
    db_delete(local_to_unique(local_id))
    return [f"Done. Task {int(message[message.index(':') + 2:])} was deleted"]


def clear_list(message, settings):
    """Clear the todo database, and respond with a conformation"""
    db_clear_all()
    return[f"Done! {settings['user_name']}, your todo list has been cleared"]


def local_to_unique(local_id):
    """Take in a local_id and return the unique id"""
    return todos[local_id - 1]['unique_id']  # -1 to deal with todos being 1 indexed
