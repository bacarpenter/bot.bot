import unittest
import bot


class TestConversation(unittest.TestCase):
    def test_hello(self):
        result = bot.respond("hello")
        self.assertEqual(result, ['Hello, bcarp04!'])

    def test_goodbye(self):
        result = bot.respond("bye")
        self.assertEqual(result, ["I'll talk to you later, bcarp04"])

    def test_thanks(self):
        result = bot.respond("thank you")
        self.assertEqual(result, ["my pleasure! 🥳"])


# if __name__ == "__main__":
#     unittest.main()
