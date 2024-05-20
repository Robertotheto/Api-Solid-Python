from src.use_cases.interfaces.users_authenticate import UsersAuthenticateInterface

class UsersAuthenticateController:
    def __init__(self, users_authenticate_use_case: UsersAuthenticateInterface):
        self.users_authenticate_use_case = users_authenticate_use_case

    def authenticate(self, email: str, password: str) -> dict:
        return self.users_authenticate_use_case.authenticate(email, password)