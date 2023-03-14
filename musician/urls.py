from django.urls import path, include
from rest_framework import routers

from musician.view import MusicianViewSet

router = routers.DefaultRouter()
router.register("musicians", MusicianViewSet, basename="manage")


urlpatterns = [
    path("", include(router.urls)),
]

app_name = "musician"
