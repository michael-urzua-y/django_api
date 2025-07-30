from typing import List, Optional
from apps.users.domain.user_model import User

class UserDAO:
    @staticmethod
    def get_all() -> List[User]:
        return User.objects.all()

    @staticmethod
    def get_by_id(user_id: str) -> Optional[User]:
        try:
            return User.objects.get(user_id=user_id)
        except User.DoesNotExist:
            return None

    @staticmethod
    def create(**kwargs) -> User:
        return User.objects.create(**kwargs)

    @staticmethod
    def update(user_id: str, **kwargs) -> Optional[User]:
        try:
            user = User.objects.get(user_id=user_id)
            for key, value in kwargs.items():
                setattr(user, key, value)
            user.save()
            return user
        except User.DoesNotExist:
            return None

    @staticmethod
    def delete(user_id: str) -> bool:
        try:
            user = User.objects.get(user_id=user_id)
            user.delete()
            return True
        except User.DoesNotExist:
            return False
