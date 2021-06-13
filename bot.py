from typing import Dict
from todoList import addTodo
import discord
import os
from enum import Enum


class MessageType(Enum):
    HELLO = 0
    BYE = 1
    NEW_TASK = 2


message_types = {
    "hello": ["hi", "hello", "howdy", "hey", "greetings"],
    "bye": ["bye", "latter", "goodnight", "ttyl", "see you soon"],
    "new_task": ["Add a to do", "new todo", "todo", "remind me", "to do"],
}
RESPOND_TO_UNKNOWN_MESSAGE = True

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


# Handle types of messages
@client.event
async def on_message(message) -> None:
    parsed = parseMessage(message.content)
    if message.author == client.user:  # Don't respond to own message
        return
    if parsed == None and RESPOND_TO_UNKNOWN_MESSAGE:
        await message.channel.send("Sorry, I don't recognize \"{0}\"".format(message.content))
    elif parsed == None and not RESPOND_TO_UNKNOWN_MESSAGE:
        return
    elif parsed['command'] == MessageType.HELLO:
        await message.channel.send(f"Hey {message.author.name}!")

    elif parsed['command'] == MessageType.BYE:
        await message.channel.send(f"I'll talk to you later, {message.author.name}!")

    elif parsed['command'] == MessageType.NEW_TASK:
        addTodo(parsed['value'])
        await message.channel.send(f"Copy that! I'll add this to your to do list, {message.author.name}!")

    elif RESPOND_TO_UNKNOWN_MESSAGE:  # Toggle weather or not to respond to unknown messages
        # Just using format here because I want to
        await message.channel.send("Sorry, I don't recognize \"{0}\"".format(message.content))

"""
Return message as a dict with a command and the value
"""


def parseMessage(message) -> Dict:
    parsed = {}
    cmd = None
    try:
        cmd = message[0:message.index(":")]
    except ValueError:
        cmd = message
        if cmd.lower() in message_types['hello']:
            parsed['command'] = MessageType.HELLO
            parsed['value'] = None
            return parsed
        elif cmd.lower() in message_types['bye']:
            parsed['command'] = MessageType.BYE
            parsed['value'] = None
            return parsed
        else:
            return None

    if cmd.lower() in message_types['hello']:
        parsed['command'] = MessageType.HELLO
    elif cmd.lower() in message_types['bye']:
        parsed['command'] = MessageType.BYE
    elif cmd.lower() in message_types['new_task']:
        parsed['command'] = MessageType.NEW_TASK
    else:
        return None

    parsed['value'] = message[message.index(":") + 2:]  # +2 for the space
    return parsed


# Get OAuth Token
try:
    TOKEN = os.getenv("TOKEN")
    if TOKEN is None:
        raise EnvironmentError
except EnvironmentError:
    print("ERROR: Cant find environment variable. Is $TOKEN set?")
    exit(1)


client.run(TOKEN)
