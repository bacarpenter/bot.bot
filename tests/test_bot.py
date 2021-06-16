import unittest
import bot


class TestConversation(unittest.TestCase):
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
