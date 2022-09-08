
from PasswordValidation import PasswordValidator
from ValidationData import ValidationData
from ValidationResult import ValidationResult

def test_ShouldReturnInvalidSize_whenPasswordSizeLessThanEight():
    validationData = ValidationData("abc123")
    passwordValidator = PasswordValidator()
    validationResult = passwordValidator.validate(validationData)
    assert validationResult.isValid() == False
    assert PasswordValidator.SIZE_ERROR in validationResult.getErrorMessages()
