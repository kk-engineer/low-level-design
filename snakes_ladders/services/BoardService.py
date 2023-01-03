from models import Player
from models.Board import Board
from services.GameService import GameService


class BoardService:
    def __init__(self):
        self._gameService = GameService()

    def get_player(self, game, player_id) -> Player:
        for player in game.players:
            if player.user.id == player_id:
                return player

        raise Exception("Player not found!")

    def update_board(self, board: Board, player: Player, roll_value: int) -> Board:
        curr_cell = board.get_current_cell(player)
        next_cell = board.get_next_cell(curr_cell, roll_value)
        curr_cell.remove_piece(player.pieces[0])
        next_cell.add_piece(player.pieces[0])
        return board

    def make_move(self, game_id: int, player_id: int) -> Board:
        game = self._gameService.get_game(game_id)
        roll_value = game.roll_dice()
        player = self.get_player(game, player_id)
        updated_board = self.update_board(game.board, player, roll_value)
        return updated_board
