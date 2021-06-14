from typing import Dict
from features.todoList import addTodo, readAll, readTodo
from messageTypes import MessageType
import discord
import bot
import os

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message) -> None:
    """Main method, very similar to a game loop"""
    # Get response from bot
    responses = bot.respond(message.content)
    for response in responses:
        await message.channel.send(response)


@client.event  # Get Emoji
async def on_raw_reaction_add(reaction):
    pass  # TODO and BUG


# Get OAuth Token
try:
    TOKEN = os.getenv("TOKEN")
    if TOKEN is None:
        raise EnvironmentError
except EnvironmentError:
    print("ERROR: Cant find environment variable. Is $TOKEN set?")
    exit(1)


client.run(TOKEN)
