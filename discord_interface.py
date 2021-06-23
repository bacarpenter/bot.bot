# Copyright (C) Ben Carpenter, 2021. Licensed under the MIT license.
import json
from typing import Dict
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

    if message.author == client.user:
        return

    # Get response from bot
    responses = bot.respond(message.content)
    for response in responses:
        await message.channel.send(response)


@client.event  # Get Emoji
async def on_raw_reaction_add(reaction):
    pass  # TODO and BUG


# See if running on CI server
if os.environ.get("CI") == "true":
    # Should only be run if project is on a CI server. Namely, GitHub actions
    TOKEN = os.environ.get("DISCORD_TOKEN")
else:
    # Load OAuth from JSON
    try:
        with open("secrets/discord_token.json") as settings_JSON:
            TOKEN = json.load(settings_JSON)["token"]
    except FileNotFoundError:
        print("Error: Could not open secrets/discord_token.json Is it there?")
        exit(1)
    except KeyError:
        print("Error: secrets/discord_token.json does not have a token object.")
        exit(2)


client.run(TOKEN)
