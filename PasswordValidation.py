
from ValidationData import ValidationData
from ValidationResult import ValidationResult

class PasswordValidator:

    MINIMUM_SIZE = 8
    SIZE_ERROR: str = "Password must be at least {MINIMUM_SIZE} characters"
    MINIMUM_NUMERIC_CHARACTER = 2
    NUMERIC_CHARACTER_ERROR: str = "The password must contain at least {MINIMUM_NUMERIC_CHARACTER} numbers"
    MINIMUM_CAPITAL_CHARACTER = 1
    CAPITAL_CHARACTER_ERROR: str = "password must contain at least {MINIMUM_CAPITAL_CHARACTER} capital letter"
    MINIMUM_SPECIAL_CHARACTER = 1
    SPECIAL_CHARACTER_ERROR: str = "password must contain at least {MINIMUM_SPECIAL_CHARACTER} special character"
    SPECIAL_CHARACTERS = " !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    def validate(self, validationData: ValidationData) -> ValidationResult:
        validPassword: bool = True
        errorMessages: list = []
        password = validationData.password

        if not self.passwordHasMinimumSize(password):
            validPassword = False
            errorMessages.append(self.SIZE_ERROR)
        if not self.passwordHasAtLeastMinimumNumericCharacter(password):
            validPassword = False
            errorMessages.append(self.NUMERIC_CHARACTER_ERROR)
        
        if not self.passwordHasAtLeastMinimumCapitalCharacter(password):
            validPassword = False
            errorMessages.append(self.CAPITAL_CHARACTER_ERROR)
        
        if not self.passwordHasAtLeastMinimumSpecialCharacter(password):
            validPassword = False
            errorMessages.append(self.SPECIAL_CHARACTER_ERROR)

        return ValidationResult(validPassword, errorMessages)

    def passwordHasMinimumSize(self, password: str):
        return len(password) >= self.MINIMUM_SIZE

    def passwordHasAtLeastMinimumNumericCharacter(self, password: str):
        numberOfNumericCharacters = 0
        for character in password:
            if character.isdigit():
                numberOfNumericCharacters += 1

        return numberOfNumericCharacters >= self.MINIMUM_NUMERIC_CHARACTER

    def passwordHasAtLeastMinimumCapitalCharacter(self, password: str):
        numberOfCapitalCharacters = 0
        for character in password:
            if character.isupper():
                numberOfCapitalCharacters += 1

        return numberOfCapitalCharacters >= self.MINIMUM_CAPITAL_CHARACTER

    def passwordHasAtLeastMinimumSpecialCharacter(self, password: str):
        numberOfSpecialCharacters = 0
        for character in password:
            if character in self.SPECIAL_CHARACTERS:
                numberOfSpecialCharacters += 1
        
        return numberOfSpecialCharacters >= self.MINIMUM_SPECIAL_CHARACTER
    