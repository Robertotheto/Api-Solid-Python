from src.use_cases.interfaces.token_block_list import TokenBlockListInterface

class UsersLogoutController:
    def __init__(self, token_block_list_use_case: TokenBlockListInterface):
        self.token_block_list_use_case = token_block_list_use_case

    def logout(self, jti: str) -> None:
        self.token_block_list_use_case.logout(jti)