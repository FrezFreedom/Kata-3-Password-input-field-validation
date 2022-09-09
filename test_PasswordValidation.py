
from PasswordValidation import PasswordValidator
from ValidationData import ValidationData
from ValidationResult import ValidationResult

def test_ShouldReturnInvalidSize_whenPasswordHasNotMinimumSize():
    validationData = ValidationData("abc@23")
    passwordValidator = PasswordValidator()
    validationResult = passwordValidator.validate(validationData)
    assert validationResult.isValid() == False
    assert PasswordValidator.SIZE_ERROR in validationResult.getErrorMessages()

def test_ShouldReturnValidSize_whenPasswordHasMinimumSize():
    validationData = ValidationData("Abc@235748")
    passwordValidator = PasswordValidator()
    validationResult = passwordValidator.validate(validationData)
    assert validationResult.isValid() == True
    assert PasswordValidator.SIZE_ERROR not in validationResult.getErrorMessages()

def test_ShouldReturnValidPassword_whenPasswordHasAtLeastTwoNumericCharacter():
    validationData = ValidationData("Abcde@G1G2")
    passwordValidator = PasswordValidator()
    validationResult = passwordValidator.validate(validationData)
    assert validationResult.isValid() == True
    assert PasswordValidator.NUMERIC_CHARACTER_ERROR not in validationResult.getErrorMessages()

def test_ShouldReturnInvalidPassword_whenPasswordHasLessThanTwoNumericCharacter():
    validationData = ValidationData("Abcde@G1GG")
    passwordValidator = PasswordValidator()
    validationResult = passwordValidator.validate(validationData)
    assert validationResult.isValid() == False
    assert PasswordValidator.NUMERIC_CHARACTER_ERROR in validationResult.getErrorMessages()

def test_ShouldReturnValidPassword_whenPasswordHasAtLeastOneCapitalCharacter():
    validationData = ValidationData("Abcde@ghij12")
    passwordValidator = PasswordValidator()
    validationResult = passwordValidator.validate(validationData)
    assert validationResult.isValid() == True
    assert PasswordValidator.CAPITAL_CHARACTER_ERROR not in validationResult.getErrorMessages()

def test_ShouldReturnInvalidPassword_whenPasswordHasNotAtCapitalCharacter():
    validationData = ValidationData("abcde@ghij12")
    passwordValidator = PasswordValidator()
    validationResult = passwordValidator.validate(validationData)
    assert validationResult.isValid() == False
    assert PasswordValidator.CAPITAL_CHARACTER_ERROR in validationResult.getErrorMessages()