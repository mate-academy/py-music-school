from django.contrib import admin

from musician.models import Musician


@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "instrument",
        "age",
        "date_of_applying",
        "is_adult"
    )
