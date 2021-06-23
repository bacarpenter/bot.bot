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

### Step 2: Data base

Next, we will set up a data base for your todos. This will be done with firebase, because it is free and I like it. If you haven't already, sign up for [firebase](https://firebase.google.com)

1. Create a project in the dashboard. I named mine bot.bot
2. In the project, select Firestore Database from the side bar. Select create database. Chose a location close to you, as this database will only house your data. When asked for security rules, select start in production mode. You won't need to worry about security rules for this.
3. In your project sidebar, click the cog towards the top, select "Project settings"
4. Select the service accounts tab
5. Choose "Generate new private key". This will download a .json file.
6. Copy this file into the source code, under the `secrets/` directory and rename it `firebase-adminsdk.json`

Phew, now the database should be setup!

**Optional**: With this step done you can use the bot in it's CLI form. Todo this, run `python3 cli.py`. Make sure to add a todo before you try to read them.

### Step 3: Discord setup

To set up the discord bot, please follow [this](https://www.freecodecamp.org/news/create-a-discord-bot-with-python/) tutorial, up until the heading "How to Code a Basic Discord Bot with the discord.py Library". Save the token. Then, create a new file, named `discord_token.json` under the `secrets/` directory. Use the following template:

```json
{
  "token": "[TOKEN]"
}
```

and fill in `[TOKEN]` with your actual token!

### Step 4: Use

Now, you are ready to use the bot. Start talk to it through discord by using

```bash
python3 discord_interface.py
```

or, use the CLI with

```bash
python3 cli.py
```

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
