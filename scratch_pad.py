import bot


def main():
    bot.load_settings(None, {
        "user_name": "user",
        "reply_to_unknown": True
    })
    results = bot.respond("hello")
    for resault in results:
        print(resault)


if __name__ == "__main__":
    main()
