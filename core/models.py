from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import UserManager


class UserModel(AbstractUser):
    first_name = models.CharField(max_length=20, verbose_name='first_name')
    last_name = models.CharField(max_length=20, verbose_name='last_name')
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    objects = UserManager()
