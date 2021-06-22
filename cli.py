# Copyright (C) Ben Carpenter, 2021. Licensed under the MIT license.
import bot

# Rich code from the rich docs! https://rich.readthedocs.io/en/latest/markdown.html

from rich.console import Console
from rich.markdown import Markdown


def main():
    console = Console()
    while(True):
        try:
            message = input("Message => ")
            responses = bot.respond(message)
            for response in responses:
                console.print(Markdown(response))
        except KeyboardInterrupt:
            responses = bot.respond("bye")
            for response in responses:
                print("\n" + response)
                exit(0)


if __name__ == "__main__":
    main()
