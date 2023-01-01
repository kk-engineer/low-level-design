from abc import ABC, abstractmethod

class PlayingStrategy(ABC):

    @abstractmethod
    def play(self, board):
        pass