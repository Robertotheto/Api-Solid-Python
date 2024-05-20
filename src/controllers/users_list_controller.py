from src.use_cases.interfaces.users_list import UsersListInterface

class UsersListController:
    def __init__(self, users_list_use_case: UsersListInterface):
        self.users_list_use_case = users_list_use_case

    def all_users(self) -> list[dict]:
        return self.users_list_use_case.all_users()