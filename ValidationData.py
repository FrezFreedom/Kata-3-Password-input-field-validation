
class ValidationData:

    __password: str;

    def __init__(self, password: str):
        self.__password = password

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password
