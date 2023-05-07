class User:
    def __init__(self):
        self._id = None
        self._username = None
        self._email = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
