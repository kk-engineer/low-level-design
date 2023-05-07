from models.Board import Board
from models.Game import Game
from models.GameRequest import GameRequest
from repositories.GameRepository import GameRepository


class GameService:
    def __init__(self):
        self._gameRepository = GameRepository()

    def initialise_game(self, game_request: GameRequest) -> Game:
        board = Board(game_request.board_size, game_request.special_cells)
        players = game_request.players
        dices = game_request.dices

        return Game().set_board(board).set_players(players).set_dices(dices)

    def create_game(self, game_request: GameRequest):
        game = self.initialise_game(game_request)
        return self._gameRepository.save(game)

    def get_game(self, game_id: int) -> Game:
        return self._gameRepository.find_by_id(game_id)
