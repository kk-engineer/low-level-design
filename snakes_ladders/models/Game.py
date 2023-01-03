from models.Board import Board
from models.Builder import builder


class Game:
    def __init__(self):
        self._id = None
        self._board = None
        self._players = []
        self._dices = []

    @property
    def id(self):
        return self._id

    @id.setter
    def index(self, value):
        self._id = value

    @property
    def board(self):
        return self._board

    @board.setter
    def index(self, value):
        self._board = value

    @property
    def players(self):
        return self._players

    @players.setter
    def players(self, value):
        self._players = value

    @property
    def dices(self):
        return self._dices

    @players.setter
    def dices(self, value):
        self._dices = value

    # Builder methods
    @builder
    def set_board(self, board: Board):
        self._board = board

    @property
    def players(self):
        return self._players

    @players.setter
    def index(self, value):
        self._players = value

    @builder
    def set_players(self, players):
        self._players = players

    @builder
    def set_dices(self, dices):
        self._dices = dices

    def roll_dice(self) -> int:
        roll_value = 0
        for dice in self._dices:
            roll_value += dice.roll()

        return roll_value
