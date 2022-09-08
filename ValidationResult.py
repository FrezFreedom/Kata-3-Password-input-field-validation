
class ValidationResult:
    __valid: bool;
    __errorMessages: list;

    def __init__(self, valid: bool = False, errorMessages: list = []):
        self.__valid = valid
        self.__errorMessages = errorMessages

    def isValid(self):
        return self.__valid

    def getErrorMessages(self):
        return '\n'.join(self.__errorMessages)
