from services.GameService import GameService


class GameController:
    def __init__(self):
        self._game_service = GameService()

    def create_game(self, game_request):
        return self._game_service.create_game(game_request)
