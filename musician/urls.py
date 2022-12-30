from rest_framework import routers
from django.urls import path, include

from musician.view import MusicianViewSet

router = routers.DefaultRouter()
router.register("musicians", MusicianViewSet, "manage")

urlpatterns = [
    path("", include(router.urls))
]

app_name = "musician"
