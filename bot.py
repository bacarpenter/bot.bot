from features.todoList import addTodo, readAll, readTodo
from typing import List
from messageTypes import MessageType, assignType


def respond(message) -> str:
    """ 
    Take in the text of a message, and come up with the bot's responce to it.
    Because Python 3.9 does not have a switch statement (why? 😫) I will be using this
    as a "disbatch" station, for context specific methods. That way, I can avoid a very
    long elif statement, and seporate out functions.
    """
    messageType = assignType(message.content)

    response_methods = {
        MessageType.HELLO: hello,
        MessageType.BYE: bye,
        MessageType.NEW_TASK: new_task,
        MessageType.THANKS: thanks,
        MessageType.READ: read,
    }

    return response_methods['messageType'](message)


def hello(message: str) -> List:
    return ["Hello, bcarp04!"]


def bye(message: str) -> List:
    return ["I'll talk to you later, bcarp04"]


def new_task(message: str) -> List:
    rList = []
    id = addTodo(message[message.index(":") + 2:])
    rList.append(f"Copy that! I'll add this to your to do list, bcarp04!")
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
