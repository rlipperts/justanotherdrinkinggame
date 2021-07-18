from jadg.model.user_model.user_model import User, UserModel
import unittest

class TestGame(unittest.TestCase):

    def test_user_creation(self):
        user = User("Bob")
        self.assertEqual(user.name, "Bob")
        self.assertEqual(user.sip_counter, 0)

    def test_user_model(self):
        user_names = ["Karl", "Ulli", "Ute"]
        um = UserModel.from_names(user_names)
        self.assertEqual(len(um.users), 3)
        for user in um.users:
            self.assertTrue(user.name in user_names)


if __name__ == '__main__':
    unittest.main()
