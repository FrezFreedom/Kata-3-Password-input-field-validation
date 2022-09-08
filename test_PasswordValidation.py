
from PasswordValidation import PasswordValidator
from ValidationData import ValidationData
from ValidationResult import ValidationResult

def test_ShouldReturnInvalidSize_whenPasswordHasNotMinimumSize():
    validationData = ValidationData("abc123")
    passwordValidator = PasswordValidator()
    validationResult = passwordValidator.validate(validationData)
    assert validationResult.isValid() == False
    assert PasswordValidator.SIZE_ERROR in validationResult.getErrorMessages()

def test_ShouldReturnValidSize_whenPasswordHasMinimumSize():
    validationData = ValidationData("abc1235748")
    passwordValidator = PasswordValidator()
    validationResult = passwordValidator.validate(validationData)
    assert validationResult.isValid() == True
    assert PasswordValidator.SIZE_ERROR not in validationResult.getErrorMessages()