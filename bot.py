# Copyright (C) Ben Carpenter, 2021. Licensed under the MIT license.

import features.todo_list
import features.pleasantries
import features.info
import features.setup
from typing import List
from message_types import MessageType, assign_type

import json

# Load settings from JSON
with open("settings.json") as settings_JSON:
    settings = json.load(settings_JSON)


def respond(message) -> List:
    global settings
    """
    Take in the text of a message, and come up with the bot's responce to it.
    Because Python 3.9 does not have a switch statement (why? 😫) I will be using this
    as a "disbatch" station, for context specific methods. That way, I can avoid a very
    long elif statement, and seporate out functions.
    """

    # Bot setup subsection:
    if settings.get('setup'):
        # Refresh settings
        with open("settings.json") as settings_JSON:
            settings = json.load(settings_JSON)
        if settings.get('setup'):
            return features.setup.bot_setup(message, settings)

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
        MessageType.NEW_TASK: features.todo_list.new_todo,
        MessageType.THANKS: features.pleasantries.thanks,
        MessageType.READ: features.todo_list.read_all,
        MessageType.COMPLETE: features.todo_list.complete,
        MessageType.DELETE: features.todo_list.delete,
        MessageType.INFO: features.info.info,
        MessageType.CLEAR_LIST: features.todo_list.clear_list
    }

    return response_methods[message_type](message, settings)
