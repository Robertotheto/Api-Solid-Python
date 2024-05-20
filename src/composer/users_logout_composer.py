from src.repositories.token_block_list_repository import TokenBlockListRepository
from src.use_cases.token_block_list_use_case import TokenBlockListUseCase
from src.controllers.users_logout_controller import UsersLogoutController

def users_logout_composer():
    token_block_list_repository = TokenBlockListRepository()
    token_block_list_use_case = TokenBlockListUseCase(token_block_list_repository)
    return UsersLogoutController(token_block_list_use_case)