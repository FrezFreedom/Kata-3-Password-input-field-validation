
from ValidationData import ValidationData
from ValidationResult import ValidationResult

class PasswordValidator:

    def validate(validationData: ValidationData) -> ValidationResult:
        return ValidationResult(False, [])