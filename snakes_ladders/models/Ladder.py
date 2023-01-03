from models.Cell import Cell


class Ladder(Cell):
    def __init__(self):
        self._end_index = None

    def get_next_position(self) -> int:
        return self._end_index

    @property
    def end_index(self):
        return self._end_index

    @end_index.setter
    def end_index(self, value):
        self._end_index = value
