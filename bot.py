from features.todoList import addTodo, readAll, readTodo, complete as comp
from typing import List
from messageTypes import MessageType, assignType

import json

# Load settings from JSON
with open("settings.json") as settingsJSON:
    settings = json.load(settingsJSON)

RESPOND_TO_UNKNOWN_MESSAGE = settings['reply_to_unknown']


def respond(message) -> List:
    """
    Take in the text of a message, and come up with the bot's responce to it.
    Because Python 3.9 does not have a switch statement (why? 😫) I will be using this
    as a "disbatch" station, for context specific methods. That way, I can avoid a very
    long elif statement, and seporate out functions.
    """
    messageType = assignType(message)

    if messageType is None:
        if RESPOND_TO_UNKNOWN_MESSAGE:
            response = [f"Sorry, I don't understand \"{message}\""]
        else:
            response = []
        return response

    response_methods = {
        MessageType.HELLO: hello,
        MessageType.BYE: bye,
        MessageType.NEW_TASK: new_task,
        MessageType.THANKS: thanks,
        MessageType.READ: read,
        MessageType.COMPLETE: complete,
    }

    return response_methods[messageType](message)


def hello(message: str) -> List:
    return [f"Hello, {settings['user_name']}!"]


def bye(message: str) -> List:
    return [f"I'll talk to you later, {settings['user_name']}"]


def new_task(message: str) -> List:
    rList = []
    id = addTodo(message[message.index(":") + 2:])
    rList.append(
        f"Copy that! I'll add this to your to do list, {settings['user_name']}!")
    task = readTodo(id)
    rList.append(
        f"Task #{task['id']}: {task['task']}\tStatus: {'done' if task['done'] else 'todo' }")
    return rList


def thanks(message: str) -> List:
    return ["my pleasure! 🥳"]


def read(message: str) -> List:
    rList = []
    tasks = readAll()
    rList.append(f"Here's you're todos:")
    for task in tasks:
        rList.append(
            f"Task #{task['id']}: {task['task']}\tStatus: {'done' if task['done'] else 'todo' }")

    return rList


def complete(message: str) -> List:
    comp(int(message[message.index(":") + 2:]))
    task = readTodo(int(message[message.index(":") + 2:]))
    return ["Got it!", f"Task #{task['id']}: {task['task']}\tStatus: {'done' if task['done'] else 'todo' }"]
