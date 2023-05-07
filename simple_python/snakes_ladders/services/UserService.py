from models.User import User
from repositories.UserRepository import UserRepository


class UserService:
    def __init__(self):
        self._user_repository = UserRepository()

    def create_user(self, u_id: int, username: str, email: str) -> User:
        user = User()
        user.id = u_id
        user.username = username
        user.email = email
        self._user_repository.save(user)