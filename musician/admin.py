from django.contrib import admin
from .models import Musician


@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    list_display = (
        "first_name", "last_name", "instrument",
        "age", "date_of_applying"
    )
    search_fields = ("first_name", "last_name", "instrument")
    list_filter = ("instrument", "age")
