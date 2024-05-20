from src.use_cases.interfaces.users_register import UsersRegisterInterface

class UsersRegisterController:
    def __init__(self, users_register_use_case: UsersRegisterInterface):
        self.users_register_use_case = users_register_use_case

    def register(self, name: str, email: str, password: str) -> dict:
        return self.users_register_use_case.register(name, email, password)