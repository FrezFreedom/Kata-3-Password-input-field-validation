
from ValidationData import ValidationData
from ValidationResult import ValidationResult

class PasswordValidator:

    SIZE_ERROR: str = 'Password must be at least 8 characters'
    MINIMUM_SIZE = 8

    def validate(self, validationData: ValidationData) -> ValidationResult:
        password = validationData.password

        if not self.passwordHasMinimumSize(password):
            return ValidationResult(False, [self.SIZE_ERROR])

        return ValidationResult(True, [])

    def passwordHasMinimumSize(self, password: str):
        return len(password) >= self.MINIMUM_SIZE
    