from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, first_name: str, last_name: str, username: str, email: str, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        if not email:
            raise ValueError('The Email field must be set')

        if not first_name or not last_name:
            raise ValueError('Your First Name and Last Name must be set')

        user = self.model(email=self.normalize_email(email))

        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.set_password(password)
        user.is_active = True
        user.is_staff = extra_fields['is_staff']
        user.is_superuser = extra_fields['is_superuser']
        user.save()
        return user

    def create_superuser(self, first_name: str, last_name: str, username: str, email: str, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password,
            **extra_fields
        )


