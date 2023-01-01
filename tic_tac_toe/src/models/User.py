
class User:

    def __init__(self) -> None:
        self.username = None
        self.email = None
        self.photo = None
    
    def builder(func):
            def wrapper(self, *args, **kwargs):
                func(self, *args, **kwargs)
                return self
            return wrapper

    @builder
    def set_username(self, name):
        self.username = name

    @builder
    def set_email(self, email):
        self.email = email 
    
    @builder
    def set_photo(self, photo):
        self.photo = photo

    