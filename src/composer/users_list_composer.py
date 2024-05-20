from src.repositories.user_repository import UsersRepository
from src.use_cases.users_list_use_case import UsersListUseCase
from src.repositories.token_block_list_repository import TokenBlockListRepository
from src.controllers.users_list_controller import UsersListController

def users_list_composer():
    users_repository = UsersRepository()
    token_block_list_repository = TokenBlockListRepository()
    users_list_use_case = UsersListUseCase(users_repository, token_block_list_repository)
    return UsersListController(users_list_use_case)