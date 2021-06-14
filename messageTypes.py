from enum import Enum


class MessageType(Enum):
    HELLO = 0
    BYE = 1
    NEW_TASK = 2
    THANKS = 3
    READ = 4


message_types = {

    MessageType.HELLO: ["hi", "hello", "howdy", "hey", "greetings"],
    MessageType.BYE: ["bye", "latter", "goodnight", "ttyl", "see you soon"],
    MessageType.NEW_TASK: ["add a to do", "new todo", "todo", "remind me", "to do"],
    MessageType.THANKS: ["thanks", "thank you", "thx", "thanks"],
    MessageType.READ: ["what are my todos", "read all", "what's todo"],
}


def assignType(message: str) -> MessageType:
    """Return the type of the message, or None if message is unknown """
    if message.index(":") is not None:
        if message[0:message.index(":")] in message_types[MessageType.NEW_TASK]:
            return MessageType.NEW_TASK
    elif message in message_types[MessageType.HELLO]:
        return MessageType.HELLO
    elif message in message_types[MessageType.BYE]:
        return MessageType.BYE
    elif message in message_types[MessageType.THANKS]:
        return MessageType.THANKS
    elif message in message_types[MessageType.READ]:
        return MessageType.READ
    else:
        return None
