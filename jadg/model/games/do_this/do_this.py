from jadg.api.game_communication import Message, TimerMessage
from jadg.model.game import Game

from jadg.model.user_model.user_model import UserModel
from jadg.service.timer import Timer


class DoThis(Game):

    def __init__(self, communication_service):
        super(DoThis, self).__init__(communication_service)
        self.user_model = None

    def setup(self):
        self.user_model = UserModel.from_names(self.get_user_names())
        timer = Timer(self, 60)
        timer.start()

    def get_user_names(self) -> list[str]:
        return self.request('get_user_list').content["user_list"]

    def handle_message(self, message: Message):
        # react to only timer events by sending an action to a randomized user
        # in the future only respond to user messages by sending an action
        if isinstance(message, TimerMessage):
            # todo: Implement action examples stored in JSON and a loader for them
            #   that loader might take the user model as argument in the action requires an arbitrary amount of users
            #       it might just return the finalized text and the list of users
            user = self.user_model.random()
            self.send('<Action>')
        else:
            raise NotImplementedError('Do This cannot handle this type of event!')

    def finalize(self):
        pass
