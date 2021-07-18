import random


class UserModel:

    users: set['User']

    def __init__(self, users: set['User']):
        self.users = users

    @classmethod
    def from_names(cls, names: list[str]) -> 'UserModel':
        return cls({User(name) for name in names})

    def random(self):
        return random.choice(tuple(self.users))


class User:

    name = ''
    sip_counter = 0

    def __init__(self, name: str):
        self.name = name
        self.sip_counter = 0
