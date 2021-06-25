# Copyright (C) Ben Carpenter, 2021. Licensed under the MIT license.

import features.todo_list
import features.pleasantries
import features.info
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

    # Bot setup subsection:
    if settings.get('setup'):
        return bot_setup(message)

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


setup_stage = 0


def bot_setup(message):
    global setup_stage
    rList = []
    if setup_stage == 0:
        rList.append(
            "Hello! I'm bot.bot. I can't wait to help you out, but first we need to get some thing's set up.")
        rList.append("First, what's your name?")
        setup_stage += 1
        return rList
    elif setup_stage == 1:
        # Place holder. Write name to the settings.json
        rList.append(f"Awesome! Hello {message}")
        rList.append("Next, would you like me to reply to messages I don't understand? Or just ignore them? I will confirm every message I do understand either way. (yes/no)")
        setup_stage += 1
        return rList
    elif setup_stage == 2:
        # Place holder. Write respond setting to the settings.json
        rList.append(f"Got it. I will {'not' if message is 'yes' else ''}")
        rList.append("Next, we will need to set up a database.")
        rList.append(
            "**Step 1**: Login / create a Firebase (https://firebase.google.com/) account")
        rList.append("**Step 2**: Create a project with the \"add project\" button in the console (https://console.firebase.google.com/) This can be named what ever you want. I named mine \"bot-bot\"")
        rList.append(
            "**Step 3**: When prompted, turn off the \"Enable Google Analytics for this project\" toggle. Then chose the big, blue, create project button")
        rList.append("Ready to keep going? (Yes/No)")
        setup_stage += 1
        return rList
    elif setup_stage == 3:
        if message is "no":
            rList.append(
                "Oh no. I'm sorry to hear somethings not right. Please create an issue at https://github.com/bacarpenter/bot.bot/issues/.")
            setup_stage = 0
            return rList

        rList.append(
            "Great! Let's keep moving. Next, you will add the firestore database to this project.")
        rList.append("**Step 4**: Select \"Firestore Database\" from the left side menu, under the build subsection. Then, select the white \"Create database\" button")
        rList.append(
            "**Step 5**: Choose start in production and hit next. Then choose a location close to you. Select enable.")
        # FIXME continue from here!
