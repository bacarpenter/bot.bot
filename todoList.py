from typing import List
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Init access to db
cred = credentials.Certificate("secrets/bot-bot-firebase-adminsdk.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


def addTodo(task) -> None:
    # Get next todo id
    nextId = int(db.collection('counter').document(
        'counter').get().to_dict()['counter']) + 1

    # Create a new todo entry
    todo_ref = db.collection('tasks').document(f"task#{nextId}")
    todo_ref.set({'task': task, 'done': False})

    # +1 to counter
    db.collection('counter').document('counter').set({'counter': nextId})


def readAll() -> List:
    pass
