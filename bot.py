import discord
import requests
import json
import os

client = discord.Client()

message_types = {
    "hello": ["hi", "hello", "howdy", "hey", "greetings"],
    "bye": ["bye", "latter", "goodnight", "ttyl", "see you soon"]
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

    if message.content.lower() in message_types['bye']:
        await message.channel.send(f"I'll talk to you later, {message.author.name}!")

# Get OAuth Token
try:
    TOKEN = os.getenv("TOKEN")
    if TOKEN is None:
        raise EnvironmentError
except EnvironmentError:
    print("Cant find environment variable")


client.run(TOKEN)
