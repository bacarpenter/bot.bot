# bot.bot

A chatbot based todolist and buddy, built to facilitate other features over time.

## Usage

Setting up the bot takes 4 steps. You only need to complete step 1 if you don't need to interact with the bot through discord.

### Step 1: Basics

First, you will need to download the code and install the dependencies. Then, you will change some settings.

1. `git clone https://github.com/bacarpenter/bot.bot.git` clones the code onto your machine.
2. `pip install -r requirements.txt` installs the dependance. Note: I suggest that you use a venv to do this.
3. In the `settings.json`file, update the name that you want to bot to refer to you by. Mine is bacarp04. Then, you can change weather or not the bot should respond to messages it doesn't understand.

### Step 2: Data base

Next, we will set up a data base for your todos. This will be done with firebase, because it is free and I like it. If you haven't already, sign up for [firebase](https://firebase.google.com)

1. Create a project in the dashboard. I named mine bot.bot
2. In the project, select Firestore Database from the side bar. Select create database. Chose a location close to you, as this database will only house your data. When asked for security rules, select start in production mode. You won't need to worry about security rules for this.
3. In your project sidebar, click the cog towards the top, select "Project settings"
4. Select the service accounts tab
5. Choose "Generate new private key". This will download a .json file.
6. Copy this file into the source code, under a new directory `secrets/` and name it `firebase-adminsdk.json`

Phew, now the database should be setup!

**Optional**: With this step done you can use the bot in it's CLI form. Todo this, run `python3 cli.py`. Make sure to add a todo before you try to read them.

### Step 3: Discord

To set up the discord bot, please follow [this](https://www.freecodecamp.org/news/create-a-discord-bot-with-python/) tutorial, up until the heading "How to Code a Basic Discord Bot with the discord.py Library". Save the token.

With the bot created, now, you need to set the environment variable, to let the python script access the bot. Do this by running `export TOKEN=[your_token]` where `[your_token]` is the token you copied. Then, to start the bot, you can run `python3 discordInterface.py`

### Step 4: Hosting

You will probably want to host your bot online. While this can be done anywhere that let's you write python code, I am doing it through [repl.it](https://replit.com), and using one of my always on projects on my Hacker plan.
