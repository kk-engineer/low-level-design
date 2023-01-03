from src.models.BoardCell import BoardCell


class Board:
    def __init__(self, rows, cols) -> None:
        self.rows = rows
        self.columns = cols
        self.cells = None
        self.initialize_board()

    def initialize_board(self):
        self.cells = []
        self.cells = [[BoardCell()] * self.columns for _ in range(self.rows)]
