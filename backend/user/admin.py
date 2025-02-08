from .models import User
from django.contrib import admin

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'password', 'full_name', 'email']

