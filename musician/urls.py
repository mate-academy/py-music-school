from django.urls import path, include
from rest_framework.routers import DefaultRouter

from musician.view import MusicianViewSet

router = DefaultRouter()
router.register("manage", MusicianViewSet, basename="manage")

app_name = "musician"

urlpatterns = [
    path("", include(router.urls)),
]
