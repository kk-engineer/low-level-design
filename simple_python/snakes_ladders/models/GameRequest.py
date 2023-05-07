class GameRequest:
    def __init__(self):
        self._board_size = None
        self._players = []
        self._dices = []
        self._special_cells = []

    @property
    def special_cells(self):
        return self._special_cells

    @special_cells.setter
    def special_cells(self, value):
        self._special_cells = value

    @property
    def players(self):
        return self._players

    @players.setter
    def players(self, value):
        self._players = value

    @property
    def board_size(self):
        return self._board_size

    @board_size.setter
    def board_size(self, value):
        self._board_size = value

    @property
    def dices(self):
        return self._dices

    @dices.setter
    def dices(self, value):
        self._dices = value
