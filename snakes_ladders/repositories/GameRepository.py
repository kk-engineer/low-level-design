from models.Game import Game


class GameRepository:
    def __init__(self):
        self._games = []

    def save(self, game: Game) -> Game:
        self._games.append(game)
        return game

    def find_by_id(self, game_id: int) -> Game:
        for game in self._games:
            if game.id == game_id:
                return game
