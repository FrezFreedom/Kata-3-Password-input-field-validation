
class ValidationResult:
    __valid: bool;
    __errorMessages: list;

    def __init__(valid: bool = False, errorMessages: list = []):
        this.__valid = valid
        this.__errorMessages = errorMessages

    def isValid():
        return self.__valid

    def getErrorMessages():
        return '\n'.join(self.__errorMessages)