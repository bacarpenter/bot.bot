from typing import Dict, List
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Init access to db
cred = credentials.Certificate("secrets/firebase-adminsdk.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


def add_todo(task: str) -> int:
    # Get next todo id
    next_id = int(db.collection('counter').document(
        'counter').get().to_dict()['counter']) + 1

    # Create a new todo entry
    todo_ref = db.collection('tasks').document(f"task#{next_id}")
    todo_ref.set({'task': task, 'done': False, 'id': next_id})

    # +1 to counter
    db.collection('counter').document('counter').set({'counter': next_id})

    return next_id


def read_todo(id: int) -> Dict:
    todo_ref = db.collection('tasks').document(f"task#{id}").get().to_dict()
    return todo_ref


def read_all() -> List:
    todos_ref = db.collection('tasks').stream()
    todos = []
    for todo in todos_ref:
        todos.append(todo.to_dict())

    return todos


def complete(id: int) -> None:
    todo_ref = db.collection('tasks').document(f"task#{id}")
    todo_ref.set({'done': True, }, merge=True)