from django.contrib import admin
from .models import Board


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):

    """ Board Admin """

    list_display = (
        "writer",
        "title",
        "content",
        "created_at"
    )

