from django.urls import path, include
from rest_framework import routers

from musician.views import MusicianViewSet

music_router = routers.DefaultRouter()
music_router.register("musicians", MusicianViewSet, basename="manage")

urlpatterns = [
    path("", include(music_router.urls))
]

app_name = "musician"
