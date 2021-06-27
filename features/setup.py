setup_stage = 0


def bot_setup(message, settings):
    global setup_stage
    rList = []
    if setup_stage == 0:
        rList.append(
            "Hello! I'm bot.bot. I can't wait to help you out, but first we need to get some thing's set up.")
        rList.append("First, what's your name?")
        setup_stage += 1
        return rList
    elif setup_stage == 1:
        # Place holder. Write name to the settings.json
        rList.append(f"Awesome! Hello {message}")
        rList.append("Next, would you like me to reply to messages I don't understand? Or just ignore them? I will confirm every message I do understand either way. (yes/no)")
        setup_stage += 1
        return rList
    elif setup_stage == 2:
        # Place holder. Write respond setting to the settings.json
        # Place holder. Logic for if message is NOT 'yes' or 'no'
        rList.append(
            f"Got it. I will {'not' if message == 'no' else ''} respond to messages that I don't understand.")
        rList.append("Next, we will need to set up a database.")
        rList.append(
            "**Step 1**: Login / create a Firebase (https://firebase.google.com/) account")
        rList.append("**Step 2**: Create a project with the \"add project\" button in the console (https://console.firebase.google.com/) This can be named what ever you want. I named mine \"bot-bot\"")
        rList.append(
            "**Step 3**: When prompted, turn off the \"Enable Google Analytics for this project\" toggle. Then chose the big, blue, create project button")
        rList.append("Ready to keep going? (Yes/No)")
        setup_stage += 1
        return rList
    elif setup_stage == 3:
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
        # FIXME continue from here!
