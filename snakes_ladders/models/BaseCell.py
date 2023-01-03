from models.Cell import Cell


class BaseCell(Cell):

    def get_next_position(self) -> int:
        return self.index
