from jadg.model.logic.game import Game


class DoThis(Game):

    def __init__(self, communication_service):
        """
        Create the game class.
        Args:
            communication_service: interface to talk to the client with
        """
        super(DoThis, self).__init__(communication_service)

    def setup(self):
        """
        Begin setup of the game and its logic and data.
        """
        pass

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
