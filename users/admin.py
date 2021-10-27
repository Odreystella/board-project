from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):

    """ User Admin """

    fieldsets = UserAdmin.fieldsets + (
        ("Custom Profile", {
            "fields": (
                "name",
                "bio",
            )
        }),
    ) 

    list_display = (
       "email",
       "name",
    )

