from abc import ABC, abstractmethod

from models.Piece import Piece


class Cell(ABC):
    def __init__(self):
        self._index = None
        self._type = None
        self._pieces = []

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, value):
        self._index = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def pieces(self):
        return self._pieces

    @pieces.setter
    def pieces(self, value):
        self._pieces = value

    @abstractmethod
    def get_next_position(self) -> int:
        pass

    def remove_piece(self, piece: Piece):
        pass

    def add_piece(self, piece: Piece):
        pass
