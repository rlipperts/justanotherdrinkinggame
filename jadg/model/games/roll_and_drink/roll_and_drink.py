from jadg.model.game import Game


class RollAndDrink(Game):

    def __init__(self, communication_service):
        """
        Create the game class.
        Args:
            communication_service: interface to talk to the client with
        """
        super(RollAndDrink, self).__init__(communication_service)

    def setup(self):
        """
        Begin setup of the game and its logic and data.
        """
        pass

    def run(self):
        """
        Start the game.
        """

    def handle_event(self):
        """
        Handle an event.
        """
        pass

    def finalize(self):
        """
        End the game.
        """
        pass