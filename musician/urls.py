from django.urls import path, include
from rest_framework import routers

from musician.views import MusicianSetView

app_name = "musician"

router = routers.DefaultRouter()
router.register("musicians", MusicianSetView, basename="manage")

urlpatterns = [
    path("", include(router.urls)),
]
