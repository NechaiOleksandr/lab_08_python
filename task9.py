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

    # Методи для кроку B
    def increment_login_attempts(self):
        self.loginAttempts += 1

    def reset_login_attempts(self):
        self.loginAttempts = 0


# --- КРОК D: Клас Privileges (винесений окремо) ---
class Privileges:
    def __init__(self):
        self.privileges = [
            "Allowed to add message",
            "Allowed to delete users",
            "Allowed to ban users",
            "Allowed to modify settings"
        ]

    def show_privileges(self):
        print("\nПривілеї адміністратора:")
        for privilege in self.privileges:
            print(f"- {privilege}")


# --- КРОК C: Клас Admin (з композицією з кроку D) ---
class Admin(User):
    def __init__(self, firstName, lastName, email, username, newsletter=False):
        super().__init__(firstName, lastName, email, username, newsletter)
        self.priv = Privileges()


user1 = User("Олег", "Петренко", "oleg@mail.com", "OlegP")
user2 = User("Марія", "Іванова", "maria@mail.com", "Mari_I", newsletter=True)

user1.describe_user()
user1.greeting_user()

user2.describe_user()
user2.greeting_user()

print(f"Спроби входу (початкові): {user1.loginAttempts}")
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(f"Спроби входу (після 3-х невдалих): {user1.loginAttempts}")

user1.reset_login_attempts()
print(f"Спроби входу (після скидання): {user1.loginAttempts}")
myAdmin = Admin("Адмін", "Головний", "admin@site.com", "SuperAdmin")

myAdmin.describe_user()
myAdmin.priv.show_privileges()