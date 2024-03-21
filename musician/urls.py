from django.urls import path, include
from rest_framework import routers

from musician.views import MusicianViewSet

router = routers.SimpleRouter()

router.register(r"", MusicianViewSet, basename="manage")

urlpatterns = [path("", include(router.urls))]

app_name = "musician"
