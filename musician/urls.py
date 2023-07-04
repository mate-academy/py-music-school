from django.urls import path, include
from rest_framework import routers

from musician.views import MusicianSetView

router = routers.DefaultRouter()
router.register("musicians", MusicianSetView, basename="manage")

urlpatterns = [
    path("musicians/", include(router.urls))
]

app_name = "musician"
