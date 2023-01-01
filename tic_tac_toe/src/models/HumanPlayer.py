from src.models.Player import Player
from src.models import BoardCell

class HumanPlayer(Player):

    def __init__(self) -> None:
        self.user = None
    
    def builder(func):
            def wrapper(self, *args, **kwargs):
                func(self, *args, **kwargs)
                return self
            return wrapper

    @builder
    def set_user(self, user):
        self.user = user

    # override abstract method
    def play(self, board) -> BoardCell:
        # TODO
        #return BoardCell()
        pass