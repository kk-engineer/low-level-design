import unittest

from models.Board import Board
from models.CellType import CellType
from models.Color import Color
from models.GameRequest import GameRequest
from models.Ladder import Ladder
from models.Piece import Piece
from models.Player import Player
from models.Snake import Snake
from services.GameService import GameService


class GameServiceTest(unittest.TestCase):
    def __init__(self, method_name: str = ...) -> None:
        super().__init__(method_name)
        self._gameService = GameService()
        self._game = None
        self._game_request = None

    def create_game_request(self):
        player_1, player_2 = Player(), Player()
        player_1.color = Color.BLUE
        # pieces
        piece_1, piece_2 = Piece(), Piece()
        piece_1.color = Color.BLUE
        piece_2.color = Color.RED
        player_1.pieces = [piece_1]
        player_2.color = Color.RED
        player_2.pieces = [piece_2]

        players = [player_1, player_2]

        # special cells
        snake, ladder = Snake(), Ladder()
        snake.type, ladder.type = CellType.SNAKE, CellType.LADDER
        snake.index, ladder.index = 10, 5
        snake.end_index, ladder.end_index = 2, 41
        special_cells = [snake, ladder]

        game_request = GameRequest()
        game_request.board_size = 100
        game_request.players = players
        game_request.special_cells = special_cells

        return game_request

    def filter_cells(self, cells, cell_type):
        filtered_cells = []
        for cell in cells:
            if cell.type == cell_type:
                filtered_cells.append(cell)

        return filtered_cells

    def setUp(self) -> None:
        self._game_request = self.create_game_request()
        self._game = self._gameService.create_game(self._game_request)

    def test_players(self):
        self.assertEqual(len(self._game_request.players), len(self._game.players))

    def test_board(self):
        board = self._game.board
        self.assertEqual(self._game_request.board_size, len(board.cells))

    def test_snake_cells(self):
        board = self._game.board
        self.assertEqual(1, len(self.filter_cells(board.cells, CellType.SNAKE)), msg='{0}'.format(len(board.cells)))

    def test_ladder_cells(self):
        board = self._game.board
        self.assertEqual(1, len(self.filter_cells(board.cells, CellType.LADDER)), msg='{0}'.format(len(board.cells)))


if __name__ == '__main__':
    unittest.main()
