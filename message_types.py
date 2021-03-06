# Copyright (C) Ben Carpenter, 2021. Licensed under the MIT license.
from enum import Enum


class MessageType(Enum):
    HELLO = 0
    BYE = 1
    NEW_TASK = 2
    THANKS = 3
    READ = 4
    COMPLETE = 5
    DELETE = 6
    INFO = 7
    CLEAR_LIST = 8


message_types = {
    MessageType.HELLO: ["hi", "hello", "howdy", "hey", "greetings"],
    MessageType.BYE: ["bye", "latter", "goodnight", "ttyl", "see you soon"],
    MessageType.NEW_TASK: ["add a todo", "new todo", "todo", "remind me", "to do", "add todo", "add to do", "n"],
    MessageType.THANKS: ["thanks", "thank you", "thx", "thanks"],
    MessageType.READ: ["what are my todos?", "read all", "what's todo", "what's on my todo list?", "r"],
    MessageType.COMPLETE: ["complete", "done", "finish", "comp", "c"],
    MessageType.DELETE: ["delete", "delete todo", "del", "d"],
    MessageType.INFO: ["info", "help", "who are you?", "what is this?"],
    MessageType.CLEAR_LIST: ["CLEAR_LIST"]
}


def assign_type(message: str) -> MessageType:
    """Return the type of the message, or None if message is unknown """

    if ":" in message:
        if message[0:message.index(":")] in message_types[MessageType.NEW_TASK]:
            return MessageType.NEW_TASK
        if message[0:message.index(":")] in message_types[MessageType.COMPLETE]:
            return MessageType.COMPLETE
        if message[0:message.index(":")] in message_types[MessageType.DELETE]:
            return MessageType.DELETE
    elif message in message_types[MessageType.HELLO]:
        return MessageType.HELLO
    elif message in message_types[MessageType.BYE]:
        return MessageType.BYE
    elif message in message_types[MessageType.THANKS]:
        return MessageType.THANKS
    elif message in message_types[MessageType.READ]:
        return MessageType.READ
    elif message in message_types[MessageType.INFO]:
        return MessageType.INFO
    elif message in message_types[MessageType.CLEAR_LIST]:
        return MessageType.CLEAR_LIST
    else:
        return None
