import bot


def main():
    while(True):
        message = input("Message => ")
        responses = bot.respond(message)
        for response in responses:
            print(response)


if __name__ == "__main__":
    main()
