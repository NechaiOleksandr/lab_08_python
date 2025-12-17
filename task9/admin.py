from user import User

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
            print(f"{privilege}")


class Admin(User):
    def __init__(self, firstName, lastName, email, username, newsletter=False):
        super().__init__(firstName, lastName, email, username, newsletter)
        self.priv = Privileges()