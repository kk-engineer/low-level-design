from abc import ABC, abstractmethod

class WinningStrategy(ABC):

    @abstractmethod
    def check_winner(self, board, players):
        pass