from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Passenger
# Register your models here.


class PassengerAdmin(admin.ModelAdmin):
    model = Passenger


admin.site.register(Passenger, PassengerAdmin)