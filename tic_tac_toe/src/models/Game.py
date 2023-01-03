from src.models.Board import Board


class Game:
    def __init__(self) -> None:
        self.board = None
        self.players = []
        self.strategy = None

    class Builder:

        def __init__(self) -> None:
            self.game = Game()

        def builder(func):
            def wrapper(self, *args, **kwargs):
                func(self, *args, **kwargs)
                return self

            return wrapper

        @builder
        def with_dimension(self, rows, cols):
            self.game.board = Board(rows, cols)

        @builder
        def with_player(self, player):
            self.game.players.append(player)

        def validate(self) -> bool:
            if len(self.game.players) > 2:
                return False
            return True

        def build(self):
            is_valid = self.validate()
            if not is_valid:
                raise Exception("Game is not valid!")

            return self.game
