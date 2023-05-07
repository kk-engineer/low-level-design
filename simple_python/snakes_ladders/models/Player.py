class Player:
    def __init__(self):
        self._color = None
        self._user = None
        self._pieces = []

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        self._user = value

    @property
    def pieces(self):
        return self._pieces

    @pieces.setter
    def pieces(self, value):
        self._pieces = value
