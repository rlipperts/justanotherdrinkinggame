from abc import ABC

class Event(ABC):

    identifier: int
    content: any
