from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager


class User(AbstractUser):
    objects = UserManager()

    REQUIRED_FIELDS = []
    avatar = models.ImageField(blank=True, null=True)
    inst = models.CharField(max_length=150, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.username
