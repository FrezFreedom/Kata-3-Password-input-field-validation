
class ValidationResult:
    __valid: bool;
    __erorrMessages: list;

    def __init__(valid: bool = False, erorrMessages: list = []):
        this.__valid = valid
        this.__erorrMessages = erorrMessages

    def isValid():
        return self.__valid

    def getErorrMessages():
        return __erorrMessages