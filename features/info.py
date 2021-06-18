# Copyright (C) Ben Carpenter, 2021. Licensed under the MIT license.

from typing import List


def info(messge, settings) -> List:
    hello = "Hello! I'm bot.bot, an extendable bot built by Ben Carpenter for use with Discord."
    commands = "You can ask me to do things like add a todo: [TASK], complete: [TASK_ID] or just exchange some pleasantries."
    link = "Check me out on GitHub! https://github.com/bacarpenter/bot.bot"
    return [hello, commands, link]
