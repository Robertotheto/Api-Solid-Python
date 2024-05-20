from src.repositories.interfaces.token_block_list_repository import TokenBlockListRepositoryInterface
from src.use_cases.interfaces.token_block_list import TokenBlockListInterface

class TokenBlockListUseCase(TokenBlockListInterface):
    def __init__(self, token_block_list_repository: TokenBlockListRepositoryInterface):
        self.token_block_list_repository = token_block_list_repository

    def logout(self, jti: str) -> None:
        if jti:
            self.token_block_list_repository.insert_jti(jti)
        else:
            raise Exception('Invalid token')
