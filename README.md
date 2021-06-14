# bot.bot

A chatbot based todolist and buddy

## Usage

Setting up the bot takes 4 steps. You only need to complete step 1 if you don't need to interact with the bot through discord.

### Step 1: Basics

First, you will need to download the code and install the dependencies.

1. `git clone https://github.com/bacarpenter/bot.bot.git` clones the code onto your machine.
2. `pip install -r requirements.txt` installs the dependance. Note: I suggest that you use a venv to do this.

### Step 2: Data base

Next, we will set up a data base for your todos. This will be done with firebase, becuse it is free and I like it. If you haven't already, sign up for [firebase](https://firebase.google.com)

1. Create a project in the dashboard. I named mine bot.bot
2. In the project, select Firestore Database from the side bar. Select create database. Chose a location close to you, as this database will only house your data. When asked for security rules, select start in production mode. You won't need to worry about security rules for this.
3. In your project sidebar, click the cog towards the top, select "Project settings"
4. Select the service accounts tab
5. Choose "Generate new private key". This will download a .json file.
6. Copy this file into the source code, under a new directory `secrets/` and name it `firebase-adminsdk.json`

Phew, now the database should be setup!

**Optional**: With this step done you can use the bot in it's CLI form. Todo this, run `python3 cli.py`. Make sure to add a todo before you try to read them.

### Step 3: Discord

THIS GUIDE IS NOT DONE. WILL BE FINISHED LATER
