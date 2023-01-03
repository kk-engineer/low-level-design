from src.models.Player import Player
from src.models import BoardCell


class BotPlayer(Player):

    def __init__(self) -> None:
        self.playingStrategy = None

    def builder(func):
        def wrapper(self, *args, **kwargs):
            func(self, *args, **kwargs)
            return self

        return wrapper

    @builder
    def set_playing_strategy(self, strategy):
        self.playingStrategy = strategy

    # override abstract method
    def play(self, board) -> BoardCell:
        # TODO
        # return BoardCell()
        pass
