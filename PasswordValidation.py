
from ValidationData import ValidationData
from ValidationResult import ValidationResult

class PasswordValidator:

    SIZE_ERROR: str = 'Password must be at least 8 characters'
    TWO_NUMBERS_ERROR: str = 'The password must contain at least 2 numbers'
    CAPITAL_CHARACTER_ERROR: str = 'password must contain at least one capital letter'
    SPECIAL_CHARACTER_ERROR: str = 'password must contain at least one special character'
    
    def validate(self, validationData: ValidationData) -> ValidationResult:
        return ValidationResult(False, [])