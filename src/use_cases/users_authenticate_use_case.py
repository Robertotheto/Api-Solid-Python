from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash
from datetime import timedelta
from src.repositories.interfaces.users_repository import UsersRepositoryInterface
from src.use_cases.interfaces.users_authenticate import UsersAuthenticateInterface

class UsersAuthenticateUseCase(UsersAuthenticateInterface):
    def __init__(self, users_repository: UsersRepositoryInterface):
        self.users_repository = users_repository

    def authenticate(self, email: str, password: str) -> dict:
        user = self.users_repository.find_by_email(email)
        if user and check_password_hash(user.password, password):
            access_token = create_access_token(identity=user.id, expires_delta=timedelta(hours=1))
            return {'access_token': access_token}
        raise Exception('Invalid credentials')