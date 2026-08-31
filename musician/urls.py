from rest_framework import routers
from django.urls import path, include
from .models import Musician
from .views import MusicianViewSet

app_name = "musician"

router = routers.DefaultRouter()

router.register("musician", MusicianViewSet, basename="manage")

urlpatterns = [
    path("", include(router.urls)),
]
