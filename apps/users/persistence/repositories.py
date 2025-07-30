from typing import List, Optional
from django.db import connection
from apps.users.persistence.user_dao import UserDAO
from apps.users.domain.user_model import User
from myapi.esquemas import get_schema_for_client

class UserRepository:
    def __init__(self, schema_indicator: str = 'default'):
        self.dao = UserDAO()
        self.schema_indicator = schema_indicator

    def set_schema(self, schema_indicator: Optional[str] = None) -> None:
        schema_key = schema_indicator or self.schema_indicator
        schema = get_schema_for_client(schema_key)
        with connection.cursor() as cursor:
            cursor.execute(f'SET search_path TO {schema}')

    def get_all_users(self, schema_indicator: Optional[str] = None) -> List[User]:
        self.set_schema(schema_indicator)
        return self.dao.get_all()

    def get_user_by_id(self, user_id: str, schema_indicator: Optional[str] = None) -> Optional[User]:
        self.set_schema(schema_indicator)
        return self.dao.get_by_id(user_id)

    def create_user(self, schema_indicator: Optional[str] = None, **kwargs) -> User:
        self.set_schema(schema_indicator)
        return self.dao.create(**kwargs)

    def update_user(self, user_id: str, schema_indicator: Optional[str] = None, **kwargs) -> Optional[User]:
        self.set_schema(schema_indicator)
        return self.dao.update(user_id, **kwargs)

    def delete_user(self, user_id: str, schema_indicator: Optional[str] = None) -> bool:
        self.set_schema(schema_indicator)
        return self.dao.delete(user_id)
