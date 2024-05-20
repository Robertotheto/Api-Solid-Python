from src.database.settings import db
from src.models.users import Users
from src.repositories.interfaces.users_repository import UsersRepositoryInterface

class UserAlreadyExistsException(Exception):
    def __init__(self, email: str):
        self.email = email
        super().__init__(f"User with email {email} already exists.")

class UsersRepository(UsersRepositoryInterface):
    def create(self, name: str, email: str, password: str) -> Users:
        try:
            if (
                existing_user := db.session.query(Users)
                .filter(Users.email == email)
                .first()
            ):
                raise UserAlreadyExistsException(email)
            user = Users(name=name, email=email, password=password)
            db.session.add(user)
            db.session.commit()
            db.session.refresh(user)
            return user
        except Exception as exception:
            db.session.rollback()
            raise exception
    def find_by_email(self, email: str) -> Users:
            try:
                return db.session.query(Users).filter(Users.email == email).first()
            except Exception as exception:
                raise exception
    
    def list_users(self) -> list[Users]:
        try:
            return db.session.query(Users).all()
        except Exception as exception:
            raise exception