from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# MOdels
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password"),}),
        ("Informacion Personal", {"fields": ("first_name", "last_name", "email"),}),
        ("Contacto", {"fields": ("web_site", "twitter"),}),
        ("Permisos", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions"),}),
        ("Fechas Importantes", {"fields": ("last_login", "date_joined"),}),
    )