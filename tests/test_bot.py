# Copyright (C) Ben Carpenter, 2021. Licensed under the MIT license.
import unittest
import bot


class TestPleasantries(unittest.TestCase):
    def test_0hello(self):
        # Force settings for testing constancy
        bot.settings = {
            "user_name": "user",
            "reply_to_unknown": True
        }
        result = bot.respond("hello")
        self.assertEqual(result, ['Hello, user!'])

    def test_1goodbye(self):
        bot.settings = {
            "user_name": "user",
            "reply_to_unknown": True
        }
        result = bot.respond("bye")
        self.assertEqual(result, ["I'll talk to you later, user"])

    def test_2thanks(self):
        bot.settings = {
            "user_name": "user",
            "reply_to_unknown": True
        }
        result = bot.respond("thank you")
        self.assertEqual(result, ["my pleasure! 🥳"])

    def test_3reply_unknown(self):
        bot.settings = {
            "user_name": "user",
            "reply_to_unknown": True
        }
        result = bot.respond("1234")
        self.assertEqual(result, ["Sorry, I don't understand \"1234\""])

    def test_4no_reply_unknown(self):
        bot.settings = {
            "user_name": "user",
            "reply_to_unknown": False
        }
        result = bot.respond("1234")
        self.assertEqual(result, [])


class TestTodo(unittest.TestCase):
    task_id = -1

    def test_0add(self):
        global task_id
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

    def test_1read(self):
        bot.settings = {
            "user_name": "user",
            "reply_to_unknown": True
        }
        result = bot.respond("read all")
        self.assertEqual(
            result[-1], f"Task #{task_id}: TEST_TODO\tStatus: todo")

    def test_2complete(self):
        bot.settings = {
            "user_name": "user",
            "reply_to_unknown": True
        }
        result = bot.respond("read all")
        self.assertEqual(
            result[-1], f"Task #{task_id}: TEST_TODO\tStatus: todo")  # Make sure it's not already done

        result = bot.respond(f"complete: {task_id}")
        self.assertEqual(
            result, ['Got it!', f'Task #{task_id}: TEST_TODO\tStatus: done'])

        result = bot.respond("read all")
        self.assertEqual(
            result[-1], f"Task #{task_id}: TEST_TODO\tStatus: done")

    def test_3remove(self):
        bot.settings = {
            "user_name": "user",
            "reply_to_unknown": True
        }
        result = bot.respond(f"del: {task_id}")
        self.assertEqual(result, [f"Done. Task #{task_id} was deleted"])

        result = bot.respond("read all")
        self.assertNotEqual(
            result[-1], f"Task #{task_id}: TEST_TODO     Status: todo")
