from django.contrib.admin import register
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core.models import User


@register(User)
class UserAdmin(BaseUserAdmin):
    ordering = ["id"]
    list_display = ["id", "name", "email"]
    fieldsets = (
        (None, {"fields": ("name", "email", "password")}),
        (_("Permissions"), {"fields": ("is_active", "is_staff", "is_superuser")}),
        (_("Important dates"), {"fields": ("last_login",)}),
    )
    readonly_fields = ("last_login",)
    add_fieldsets = (
        (
            None,
            {
                "classes": "wide",
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "name",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )
