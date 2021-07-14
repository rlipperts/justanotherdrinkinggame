from jadg.event.communication import Communication
from jadg.event.event import Event
from jadg.event.game_event import GameEvent
from jadg.event.timer_event import TimerEvent
from jadg.model.game import Game
import uuid

from jadg.model.user_model.user_model import UserModel
from jadg.service.timer import Timer


class DoThis(Game):

    def __init__(self, communication_service):
        """
        Create the game class.
        Args:
            communication_service: interface to talk to the client with
        """
        super(DoThis, self).__init__(communication_service)
        self.user_model = None

    def setup(self):
        """
        Begin setup of the game and its logic and data.
        """
        self.user_model = UserModel.from_names(self.request(Communication(int(uuid.uuid4()), 'get_user_list')).content)
        timer = Timer(self, 60)
        timer.start()

    def handle_event(self, event: Event):
        """
        Handle an event.
        """
        # react to only timer events by sending an action to a randomized user
        # in the future only respond to user messages by sending an action
        if isinstance(event, TimerEvent):
            # todo: Implement action examples stored in JSON and a loader for them
            #   that loader might take the user model as argument in the action requires an arbitrary amount of users
            #       it might just return the finalized text and the list of users
            user = self.user_model.random()
            self.send(GameEvent(user, '<Action>'))
        else:
            raise NotImplementedError('Do This cannot handle this type of event!')

    def finalize(self):
        """
        End the game.
        """
        pass
