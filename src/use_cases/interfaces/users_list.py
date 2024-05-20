from abc import ABC, abstractmethod

class UsersListInterface(ABC):
    @abstractmethod
    def all_users(self) -> list[dict]:
        pass