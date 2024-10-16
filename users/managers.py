from django.contrib.auth.models import UserManager as BaseManager


class UserManager(BaseManager):
    def create_user(self, username, email, password, **extra_fields):
        if not email and not extra_fields.get("inst"):
            raise ValueError("The given email or inst must be set")
        if not username:
            raise ValueError("The given username must be set")
        if not password:
            raise ValueError("The given password must be set")
        user = super().create_user(username, email, password, **extra_fields)
        return user
