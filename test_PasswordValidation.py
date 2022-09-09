
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

def test_ShouldReturnValidPassword_whenPasswordHasAtLeastTwoNumericCharacter():
    validationData = ValidationData("AbcdefG1G2")
    passwordValidator = PasswordValidator()
    validationResult = passwordValidator.validate(validationData)
    assert validationResult.isValid() == True
    assert PasswordValidator.TWO_NUMERIC_ERROR not in validationResult.getErrorMessages()

def test_ShouldReturnInvalidPassword_whenPasswordHasLessThanTwoNumericCharacter():
    validationData = ValidationData("AbcdefG1GG")
    passwordValidator = PasswordValidator()
    validationResult = passwordValidator.validate(validationData)
    assert validationResult.isValid() == False
    assert PasswordValidator.TWO_NUMERIC_ERROR in validationResult.getErrorMessages()