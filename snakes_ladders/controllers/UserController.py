from models.User import User
from services.UserService import UserService


class UserController:
    def __init__(self):
        self._user_service = UserService()

    def create_user(self, uid: int, uname: str, email: str) -> User:
        return self._user_service.create_user(uid, uname, email)