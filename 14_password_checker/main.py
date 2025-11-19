import string


# 1. Create the blueprint
class PasswordValidator:
    def __init__(self) -> None:
        self.common_passwords: set[str] = self.load_common_passwords()

    @staticmethod
    def load_common_passwords() -> set[str]:
        with open('common_passwords.txt', 'r') as file:
            return {line.strip() for line in file if line}

    def is_common(self, password: str) -> bool:
        return password in self.common_passwords

    def rate(self, password: str) -> str:
        if self.is_common(password):
            return 'poor'

        # Calculate score
        score: int = 0
        if any(c.isupper() for c in password):  # Checks for uppercase characters
            score += 1
        if any(c in string.punctuation for c in password):  # Checks for punctuation
            score += 1
        if len(password) >= 10:  # Checks length
            score += 1

        # Return rating
        if score == 3:
            return 'secure'
        elif score == 2:
            return 'medium'
        else:
            return 'poor'


# 2. Check for password
def main() -> None:
    # Link: https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10k-most-common.txt
    validator: PasswordValidator = PasswordValidator()
    print('🔒 Welcome to the Password Strength Checker!')
    print('Enter a password to get a quality rating.')

    while True:
        password: str = input('Enter password: ').strip()
        rating: str = validator.rate(password)
        if rating == 'secure':
            print('✅ Your password is secure! ')
        elif rating == 'medium':
            print('⚠️ Your password is of medium strength.')
        else:
            print('⚠️ That password sucks!')
            print('Try adding symbols, uppercase letters, and increasing the length.')


if __name__ == '__main__':
    main()

# Homework:
# 1. Add functionality that tells the user exactly what they are missing to make their password
# stronger, such as symbols, uppercase characters, and/or more characters.
# 2. Add functionality that detects when a user adds too many sequential characters, such
# as "aaa", "111", and so on.
# 3. Check if the password contains digits as well to reach the 'secure' rating.
