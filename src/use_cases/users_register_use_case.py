from src.repositories.interfaces.users_repository import UsersRepositoryInterface
from src.use_cases.interfaces.users_register import UsersRegisterInterface
from werkzeug.security import generate_password_hash

class UsersRegisterUseCase(UsersRegisterInterface):
    def __init__(self, users_repository: UsersRepositoryInterface):
        self.users_repository = users_repository

    def register(self, name: str, email: str, password: str) -> dict:
        if self.users_repository.find_by_email(email):
            raise Exception('User already exists')
        password = generate_password_hash(password)
        user = self.users_repository.create(name, email, password)
        return formmatted_user(user)


def formmatted_user(user)-> dict:
    return {
        'id': user.id,
        'name': user.name,
        'email': user.email
    }