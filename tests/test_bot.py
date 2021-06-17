# Copyright (C) Ben Carpenter, 2021. Licensed under the MIT license.
import unittest
import bot


class TestPleasantries(unittest.TestCase):
    def test_hello(self):
        # Force settings for testing constancy
        bot.settings = {
            "user_name": "user",
            "reply_to_unknown": True
        }
        result = bot.respond("hello")
        self.assertEqual(result, ['Hello, user!'])

    def test_goodbye(self):
        bot.settings = {
            "user_name": "user",
            "reply_to_unknown": True
        }
        result = bot.respond("bye")
        self.assertEqual(result, ["I'll talk to you later, user"])

    def test_thanks(self):
        bot.settings = {
            "user_name": "user",
            "reply_to_unknown": True
        }
        result = bot.respond("thank you")
        self.assertEqual(result, ["my pleasure! 🥳"])

    def test_reply_unknown(self):
        bot.settings = {
            "user_name": "user",
            "reply_to_unknown": True
        }
        result = bot.respond("1234")
        self.assertEqual(result, ["Sorry, I don't understand \"1234\""])

    def test_no_reply_unknown(self):
        bot.settings = {
            "user_name": "user",
            "reply_to_unknown": False
        }
        result = bot.respond("1234")
        self.assertEqual(result, [])


class TestTodo(unittest.TestCase):
    task_id = None

    def test_add(self):
        bot.settings = {
            "user_name": "user",
            "reply_to_unknown": True
        }
        result = bot.respond("todo: TEST_TODO")
        # Thank you to this user https://stackoverflow.com/a/36434101/13013466
        task_id = int(''.join(filter(str.isdigit, result[1])))
        self.assertEqual(
            result[0], "Copy that! I'll add this to your to do list, user!")
        self.assertEqual(len(result), 2)
        print(task_id)

    # def test_read(self):
    #     bot.settings = {
    #         "user_name": "user",
    #         "reply_to_unknown": True
    #     }
    #     result = bot.respond("read all")
    #     self.assertTrue()

    # def test_complete(self):
    #     bot.settings = {
    #         "user_name": "user",
    #         "reply_to_unknown": True
    #     }

    # def test_remove(self):
    #     bot.settings = {
    #         "user_name": "user",
    #         "reply_to_unknown": True
    #     }
