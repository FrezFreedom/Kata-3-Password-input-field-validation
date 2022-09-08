
from ValidationData import ValidationData
from ValidationResult import ValidationResult

class PasswordValidator:

    SIZE_ERROR: str = 'Password must be at least 8 characters'
    TWO_NUMBERS_ERROR: str = 'The password must contain at least 2 numbers'
    CAPITAL_CHARACTER_ERROR: str = 'password must contain at least one capital letter'
    SPECIAL_CHARACTER_ERROR: str = 'password must contain at least one special character'
    
    def validate(self, validationData: ValidationData) -> ValidationResult:
        validPassword: bool = True
        errorMessages: list = []
        password = validationData.password

        if not self.passwordHasMoreThanSevenCharacter(password):
            validPassword = False
            errorMessages.append(self.SIZE_ERROR)

        return ValidationResult(validPassword, errorMessages)

    def passwordHasMoreThanSevenCharacter(self, password: str):
        return len(password) > 7
    