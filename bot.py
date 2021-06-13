import discord
import requests
import json
import os

RESPOND_TO_UNKNOWN_MESSAGE = True

client = discord.Client()

message_types = {
    "hello": ["hi", "hello", "howdy", "hey", "greetings"],
    "bye": ["bye", "latter", "goodnight", "ttyl", "see you soon"],
    "new_task": ["Add a to do", "new todo", "todo", "remind me", "to do"],
}


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


# Handle types of messages
@client.event
async def on_message(message):
    if message.author == client.user:  # Don't respond to own message
        return

    if message.content.lower() in message_types['hello']:
        await message.channel.send(f"Hey {message.author.name}!")

    elif message.content.lower() in message_types['bye']:
        await message.channel.send(f"I'll talk to you later, {message.author.name}!")

    elif message.content.lower() in message_types['new_task']:
        await message.channel.send(f"Copy that! I'll add this to your to do list, {message.author.name}!")

    elif RESPOND_TO_UNKNOWN_MESSAGE:
        await message.channel.send("Sorry, I don't recognize \"{0}\"".format(message.content))

# Get OAuth Token
try:
    TOKEN = os.getenv("TOKEN")
    if TOKEN is None:
        raise EnvironmentError
except EnvironmentError:
    print("ERROR: Cant find environment variable. Is $TOKEN set?")
    exit(1)


client.run(TOKEN)
