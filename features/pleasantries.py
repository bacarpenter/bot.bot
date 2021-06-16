from typing import List


def hello(message: str, settings) -> List:
    return [f"Hello, {settings['user_name']}!"]


def bye(message: str, settings) -> List:
    return [f"I'll talk to you later, {settings['user_name']}"]


def thanks(message: str, settings) -> List:
    return ["my pleasure! 🥳"]
