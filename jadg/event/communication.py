from jadg.event.event import Event


class Communication(Event):

    # todo: this needs a better name. Event to communicate between server and client without user interaction
    #   basically to request some data
    #   shouldnt we generally rename 'event' to 'message'?

    def __init__(self, identifier: int, content: str):
        self.identifier = identifier
        self.content = content
