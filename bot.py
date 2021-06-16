# Copyright (C) Ben Carpenter, 2021. Licensed under the MIT license.

import features.todo_list
import features.pleasantries
from typing import List
from message_types import MessageType, assign_type

import json

# Load settings from JSON
with open("settings.json") as settings_JSON:
    settings = json.load(settings_JSON)


def respond(message) -> List:
    """
    Take in the text of a message, and come up with the bot's responce to it.
    Because Python 3.9 does not have a switch statement (why? 😫) I will be using this
    as a "disbatch" station, for context specific methods. That way, I can avoid a very
    long elif statement, and seporate out functions.
    """
    message_type = assign_type(message)

    if message_type is None:
        if settings['reply_to_unknown']:
            response = [f"Sorry, I don't understand \"{message}\""]
        else:
            response = []
        return response

    response_methods = {
        MessageType.HELLO: features.pleasantries.hello,
        MessageType.BYE: features.pleasantries.bye,
        MessageType.NEW_TASK: features.todo_list.new_task,
        MessageType.THANKS: features.pleasantries.thanks,
        MessageType.READ: features.todo_list.read,
        MessageType.COMPLETE: features.todo_list.complete,
    }

    return response_methods[message_type](message, settings)
