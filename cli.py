import bot


def main():
    while(True):
        try:
            message = input("Message => ")
            responses = bot.respond(message)
            for response in responses:
                print(response)
        except KeyboardInterrupt:
            responses = bot.respond("bye")
            for response in responses:
                print("\n", response)
                exit(0)


if __name__ == "__main__":
    main()
