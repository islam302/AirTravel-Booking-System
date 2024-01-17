from django.contrib import admin
from .models import UserModel
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# Register your models here.
@admin.register(UserModel)
class UserAdmin(BaseUserAdmin):
    pass
