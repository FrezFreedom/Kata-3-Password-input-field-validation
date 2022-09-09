
from ValidationData import ValidationData
from ValidationResult import ValidationResult

class PasswordValidator:

    SIZE_ERROR: str = 'Password must be at least 8 characters'
    TWO_NUMBERS_ERROR: str = 'The password must contain at least 2 numbers'
    MINIMUM_SIZE = 8
    MINIMUM_NUMERIC_CHARACTER = 2

    def validate(self, validationData: ValidationData) -> ValidationResult:
        validPassword: bool = True
        errorMessages: list = []
        password = validationData.password

        if not self.passwordHasMinimumSize(password):
            validPassword = False
            errorMessages.append(self.SIZE_ERROR)
        if not self.passwordHasAtLeastMinimumNumberCharacter(password):
            validPassword = False
            errorMessages.append(self.TWO_NUMBERS_ERROR)

        return ValidationResult(validPassword, errorMessages)

    def passwordHasMinimumSize(self, password: str):
        return len(password) >= self.MINIMUM_SIZE

    def passwordHasAtLeastMinimumNumberCharacter(self, password:str):
        numberOfNumericCharacters = 0
        for character in password:
            if character.isdigit():
                numberOfNumericCharacters += 1

        return numberOfNumericCharacters >= self.MINIMUM_NUMERIC_CHARACTER
    