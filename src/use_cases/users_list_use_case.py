from flask_jwt_extended import get_jwt
from src.repositories.interfaces.users_repository import UsersRepositoryInterface
from src.use_cases.interfaces.users_list import UsersListInterface
from src.repositories.interfaces.token_block_list_repository import TokenBlockListRepositoryInterface

class UsersListUseCase(UsersListInterface):
    def __init__(self, users_repository: UsersRepositoryInterface, token_block_list_repository: TokenBlockListRepositoryInterface):
        self.users_repository = users_repository
        self.token_block_list_repository = token_block_list_repository

    def all_users(self) -> list[dict]:
        jti = get_jwt()['jti']
        if token := self.token_block_list_repository.compare_jti(jti):
            raise Exception('Invalid token')
        users = self.users_repository.list_users()
        return formatted_users_list(users)

def formatted_users_list(users: list) -> list[dict]:
    formatted_list = []
    for user in users:
        if isinstance(user, dict):
            formatted_list.append({
                'id': user['id'],
                'name': user['name'],
                'email': user['email'],
            })
        else:
            formatted_list.append({
                'id': user.id,
                'name': user.name,
                'email': user.email,
            })
    return formatted_list