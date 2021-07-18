from jadg.api.game_communication import Message
from jadg.model.game import Game


class RollAndDrink(Game):

    def __init__(self, communication_service):
        super(RollAndDrink, self).__init__(communication_service)

    def setup(self):
        pass

    def handle_message(self, message: Message):
        pass

    def finalize(self):
        pass