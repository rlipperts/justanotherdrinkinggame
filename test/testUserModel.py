from jadg.model.user_model.user_model import User, UserModel
import unittest

class TestGame(unittest.TestCase):

    def test_user_creation(self):
        user = User("Bob")
        self.assertEqual(user.name, "Bob")
        self.assertEqual(user.sip_counter, 0)

    def test_user_model(self):
        um = UserModel.from_names(["Karl", "Ulli", "Ute"])
        self.assertEqual(len(um.users), 3)


if __name__ == '__main__':
    unittest.main()
