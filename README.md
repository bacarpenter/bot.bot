# bot.bot

A chatbot based todo list and buddy, built to facilitate other features over time.

## Features

- Discord Interface
- CLI Interface
- To Do List

_And more to come :)_

## Run Locally

### Step 1: Basics

```bash
  git clone https://github.com/bacarpenter/bot.bot.git
```

Go to the project directory

```bash
  cd bot.bot
```

Install dependencies

```bash
  python3 -m pip install -r requirements.txt
```

### Step 2: Discord setup

To set up the discord bot, please follow [this](https://www.freecodecamp.org/news/create-a-discord-bot-with-python/) tutorial, up until the heading "How to Code a Basic Discord Bot with the discord.py Library". Save the token. Then, create a new file, named `discord_token.json` under the `secrets/` directory. Use the following template:

```json
{
  "token": "[TOKEN]"
}
```

### Step 4: Use

Now, you are ready to use the bot. Start talk to it through discord by using

```bash
python3 discord_interface.py
```

or, use the CLI with

```bash
python3 cli.py
```

The bot will walk you through the rest of the setup.

## Deployment

To deploy this project, I use repl.it free hacker plan for students. Learn more about setting up a Repl.it [here](https://docs.replit.com/tutorials/01-introduction-to-the-repl-it-ide). And getting your free, time limited, hacker plan [here](https://education.github.com).

Alternatively, any PaaS provider that allows for always online python projects should work just fine!

## Tech Stack

**Client:** Discord

**Server:** Python, Discord.py, Firebase

## Security

Make sure not to share anything in the `secrets/` directory publicly online!

## Acknowledgements

Thank you to...

- [readme.so](https://readme.so) for helping to create this readme.
- [freecodecamp.org](https://www.freecodecamp.org/newscreate-a-discord-bot-with-python/) for demonstrating how to use discord bots

## License

Licensed under the MIT license. [Learn more about the MIT license](https://choosealicense.com/licenses/mit/)
