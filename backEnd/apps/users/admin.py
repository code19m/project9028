from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from apps.users.models import User


class MyUserAdmin(UserAdmin):
    """Customized User Admin"""

    fieldsets = (
        (None, {"fields": ("username",)}),
        (_("Personal info"), {
            "fields": (
                "first_name", "last_name", "email", "image", "phone_number", "roles"
            )
        }),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    readonly_fields = ("last_login", "date_joined")
    list_display = ("username", "email", "first_name", "last_name", "roles")
    list_filter = ("roles",)
    search_fields = ("username", "first_name", "last_name", "email", "roles")

admin.site.register(User, MyUserAdmin)
