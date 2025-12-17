from user import User
from admin import Admin

user1 = User("Іван", "Петренко", "ivan@mail.com", "Ivan")
user2 = User("Петро", "Іваненко", "petro@mail.com", "Petro", newsletter=True)
user1.describe_user()
user1.greeting_user()
user2.describe_user()
user2.greeting_user()

print(f"Спроби входу (початкові): {user1.loginAttempts}")
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(f"Спроби входу (після кількох невдалих): {user1.loginAttempts}")
user1.reset_login_attempts()
print(f"Спроби входу (після скидання): {user1.loginAttempts}")

admin = Admin("Адмін", "Головний", "admin@site.com", "SuperAdmin")

admin.describe_user()
admin.priv.show_privileges()