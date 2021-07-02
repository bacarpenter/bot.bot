# setup_flow_text

Text to make writing `features/setup.py` easier, because hard coding strings into python is difficult.

## Settings

- Hello! I'm bot.bot. I can't wait to help you out, but first we need to get some thing's set up.
- First, what's your name?
  - Response is set as `name`
- Awesome! Hello {message}
- Next, would you like me to reply to messages I don't understand? Or just ignore them? I will confirm every message I do understand either way. (yes/No)
  - Response is set as `respond_to_unknown`

## Discord Bot Setup

## Firebase Setup

- Next, we will need to set up a database.
- **Step 1**: Login / create a Firebase (https://firebase.google.com/) account
- **Step 2**: Create a project with the \"add project\" button in the console (https://console.firebase.google.com/) This can be named what ever you want. I named mine \"bot-bot\""
- **Step 3**: When prompted, turn off the \"Enable Google Analytics for this project\" toggle. Then chose the big, blue, create project button
- Next, you will add the firestore database to this project.
- **Step 4**: Select \"Firestore Database\" from the left side menu, under the build subsection. Then, select the white \"Create database\" button"
- **Step 5**: Choose start in production and hit next. Then choose a location close to you. Select enable.
- Now, we'll give me (the bot) access to this database.
- Select the settings cog in the top left, and then project settings from the drop right menu. Under the project settings heading, choose the \"service account\" tab. Then choose the big blue \"Generate new private key\" button. Save the downloaded file.
- Rename the downloaded file exactly `firebase-adminsdk.json` and place it in the `{__file__.replace('features/setup.py', '')}secrets/` directory on your computer. This file should be kept secret, so don't post it online. <!-- **file** from https://stackoverflow.com/a/56799977/13013466. Thanks! <-- Add that to the text -- >
