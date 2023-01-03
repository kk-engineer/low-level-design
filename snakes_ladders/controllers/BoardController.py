from models.Board import Board
from services.BoardService import BoardService


class BoardController:
    def __init__(self):
        self._board_service = BoardService()

    def make_move(self, game_id: int, player_id: int) -> Board:
        return self._board_service.make_move(game_id, player_id)