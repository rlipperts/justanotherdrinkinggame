from jadg.model.user_model.user_model import User, UserModel
import unittest

class TestUserModel(unittest.TestCase):

    def setUp(self) -> None:
        self.user_names = ["Karl", "Ulli", "Ute"]
        self.user_model = UserModel.from_names(self.user_names)

    def test_user_creation(self):
        user = User("Bob")
        self.assertEqual(user.name, "Bob")
        self.assertEqual(user.sip_counter, 0)

    def test_user_model(self):
        self.assertEqual(len(self.user_model.users), 3)
        for user in self.user_model.users:
            self.assertTrue(user.name in self.user_names)

    def test_get_random_user(self):
        user = self.user_model.random()
        self.assertIn(user, self.user_model.users)


if __name__ == '__main__':
    unittest.main()
