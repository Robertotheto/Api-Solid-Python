from abc import ABC, abstractmethod
from src.models.users import Users

class UsersRepositoryInterface(ABC):
    @abstractmethod
    def create(self, name: str, email: str, password:str) -> Users:
        pass
    
    @abstractmethod
    def find_by_email(self, email: str) -> Users:
        pass

    @abstractmethod
    def list_users(self) -> list[Users]:
        pass