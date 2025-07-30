from typing import List, Optional
from apps.users.persistence.repositories import UserRepository
from apps.users.domain.user_model import User

class UserService:
    
    # manejar la lógica de negocio.
    #Esta función se comunica con la capa de persistencia
    
    def __init__(self, schema_indicator: str = 'default'):
        self.repository = UserRepository(schema_indicator)

    def list_users(self) -> List[User]:
        return self.repository.get_all_users()

    def get_user(self, user_id: str) -> Optional[User]:
        return self.repository.get_user_by_id(user_id)

    def create_user(self, **kwargs) -> User:
        return self.repository.create_user(**kwargs)

    def update_user(self, user_id: str, **kwargs) -> Optional[User]:
        return self.repository.update_user(user_id, **kwargs)

    def delete_user(self, user_id: str) -> bool:
        return self.repository.delete_user(user_id)
