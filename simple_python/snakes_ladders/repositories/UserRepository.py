from models.User import User


class UserRepository:
    def __init__(self):
        self._users = []

    def save(self, user: User):
        self._users.append(user)
