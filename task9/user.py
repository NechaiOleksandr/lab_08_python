class User:
    def __init__(self, firstName, lastName, email, username, newsletter=False):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.username = username
        self.newsletter = newsletter
        self.loginAttempts = 0

    def describe_user(self):
        print(f"\nКористувач: {self.firstName} {self.lastName}")
        print(f"Нікнейм: {self.username}")
        print(f"Email: {self.email}")
        print(f"Підписка на новини: {'Так' if self.newsletter else 'Ні'}")

    def greeting_user(self):
        print(f"Привіт, {self.username}! Раді бачити тебе знову.")

    def increment_login_attempts(self):
        self.loginAttempts += 1

    def reset_login_attempts(self):
        self.loginAttempts = 0