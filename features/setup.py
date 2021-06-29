import json


setup_stage = 0


def bot_setup(message, settings):
    """A guided setup for the bot."""
    global setup_stage
    rList = []
    if setup_stage == 0:  # Name
        rList.append(
            "Hello! I'm bot.bot. I can't wait to help you out, but first we need to get some thing's set up.")
        rList.append("First, what's your name?")
        setup_stage += 1
        return rList

    elif setup_stage == 1:  # Reply to unknown
        write_setting("user_name", message)
        rList.append(f"Awesome! Hello {message}")
        rList.append("Next, would you like me to reply to messages I don't understand? Or just ignore them? I will confirm every message I do understand either way. (yes/No)")
        setup_stage += 1
        return rList

    elif setup_stage == 2:  # Firestore pt 1
        if message.lower() == 'no':
            write_setting("reply_to_unknown", False)
        else:
            write_setting("reply_to_unknown", True)
        rList.append(
            f"Got it. I **will {'not' if message.lower() == 'no' else ''}** respond to messages that I don't understand.")
        rList.append("Next, we will need to set up a database.")
        rList.append(
            "**Step 1**: Login / create a Firebase (https://firebase.google.com/) account")
        rList.append("**Step 2**: Create a project with the \"add project\" button in the console (https://console.firebase.google.com/) This can be named what ever you want. I named mine \"bot-bot\"")
        rList.append(
            "**Step 3**: When prompted, turn off the \"Enable Google Analytics for this project\" toggle. Then chose the big, blue, create project button")
        rList.append("Ready to keep going? (Yes/no)")
        setup_stage += 1
        return rList

    elif setup_stage == 3:  # Firestore pt 2
        if message == "no":
            rList.append(
                "Oh no. I'm sorry to hear somethings not right. Please create an issue at https://github.com/bacarpenter/bot.bot/issues.")
            setup_stage = 0
            return rList

        rList.append(
            "Great! Let's keep moving. Next, you will add the firestore database to this project.")
        rList.append("**Step 4**: Select \"Firestore Database\" from the left side menu, under the build subsection. Then, select the white \"Create database\" button")
        rList.append(
            "**Step 5**: Choose start in production and hit next. Then choose a location close to you. Select enable.")
        rList.append("Ready to keep going? (Yes/no)")
        setup_stage += 1
        return rList

    elif setup_stage == 4:  # Firestore pt 3
        if message == "no":
            rList.append(
                "Oh no. I'm sorry to hear somethings not right. Please create an issue at https://github.com/bacarpenter/bot.bot/issues. Setup will now restart. Send any message to start again.")
            setup_stage = 0
            return rList

        rList.append(
            "Awesome. Now, we'll give me (the bot) access to this database.")
        rList.append("Select the settings cog in the top left, and then project settings from the drop right menu. Under the project settings heading, choose the \"service account\" tab. Then choose the big blue \"Generate new private key\" button. Save the downloaded file. ")
        rList.append(
            f"Rename the downloaded file exactly `firebase-adminsdk.json` and place it in the `{__file__.replace('features/setup.py', '')}secrets/` directory on your computer. This file should be kept secret, so don't post it online.")  # __file__ from https://stackoverflow.com/a/56799977/13013466. Thanks!
        rList.append("When you are ready to move on, please send any message.")
        setup_stage += 1
        return rList

    elif setup_stage == 5:  # Discord
        # TODO Add Discord setup
        setup_stage += 1

    elif setup_stage == 6:  # Get started
        rList.append(
            "Perfect. Let's get to work. Make your first todo with `todo: [some todo]`. It's a pleasure to meet you.")
        write_setting("setup", False)
        return rList


def write_setting(key, value):
    """Write a setting with given key and value to `settings.json` on disk."""

    # Thanks to Kite for help with this code. https://www.kite.com/python/answers/how-to-update-a-json-file-in-python

    with open("settings.json", "r") as settingsJSON:
        json_object = json.load(settingsJSON)

    json_object[key] = value

    with open("settings.json", "w") as settingsJSON:
        json.dump(json_object, settingsJSON)
