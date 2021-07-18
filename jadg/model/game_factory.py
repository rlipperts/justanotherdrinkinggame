from jadg.model.games.do_this.do_this import DoThis
from jadg.model.games.roll_and_drink.roll_and_drink import RollAndDrink


class GameFactory:

    def __init__(self):
        pass

    def new_game(self, name: str, communication_service):
        if name== 'roll and drink':
            return RollAndDrink(communication_service)
        elif name== 'do this':
            return DoThis(communication_service)
        else:
            raise NotImplementedError('The game %s does not exist!' % name)