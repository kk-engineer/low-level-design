from models import Player
from models.Cell import Cell
from models.BaseCell import BaseCell
from models.CellType import CellType


class Board:
    def parse_special_cells(self, cells):
        special_cells = {}
        for cell in cells:
            special_cells[cell.index] = cell

        return special_cells

    def create_board(self, size, special_cells):
        cells = []
        for index in range(size):
            cell = self._construct_cell(index, special_cells)
            cell.index = index
            cells.append(cell)

        return cells

    def __init__(self, size, special_cells):
        self._cells = self.create_board(size, self.parse_special_cells(special_cells))

    @property
    def cells(self):
        return self._cells

    @cells.setter
    def cells(self, value):
        self._cells = value

    def _construct_cell(self, index, special_cells) -> Cell:
        if index in special_cells.keys():
            return special_cells[index]

        base_cell = BaseCell()
        base_cell.type = CellType.BASE
        base_cell.index = index
        return base_cell

    def get_current_cell(self, player: Player) -> Cell:
        for cell in self._cells:
            if player.pieces[0] in cell.pieces:
                return cell
        raise Exception("Player not found!")

    def get_next_cell(self, current_cell: Cell, rollValue: int) -> Cell:
        return None
