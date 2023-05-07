import unittest
import sys

sys.path.append("..")
from ..src.models.Game import Game
from ..src.models.HumanPlayer import HumanPlayer
from ..src.models.BotPlayer import BotPlayer
from ..src.models.User import User
from ..src.strategies.DefaultPlayingStrategy import DefaultPlayingStrategy


class TestTicTacToe(unittest.TestCase):

    def __init__(self, method_name: str = ...) -> None:
        super().__init__(method_name)
        self.user = self.create_user()
        self.game = self.create_game()

    def create_user(self):
        user_kk = User().set_username('Karan') \
            .set_email('kk@test.com') \
            .set_photo('@#$%')

        return user_kk

    def create_game(self):
        human = HumanPlayer().set_user(self.user)
        bot = BotPlayer().set_playing_strategy(DefaultPlayingStrategy())
        game = Game().Builder() \
            .with_dimension(4, 4) \
            .with_player(human) \
            .with_player(bot) \
            .build()

        return game

    def test_dimension(self):
        cells_test = self.game.board.cells
        self.assertEqual(len(cells_test), 4)

        cell_row = cells_test[0]
        self.assertEqual(len(cell_row), 4)

    def test_players(self):
        self.assertEqual(len(self.game.players), 2)

    def test_user(self):
        self.assertEqual(self.user.username, 'Karan')


if __name__ == '__main__':
    unittest.main()
