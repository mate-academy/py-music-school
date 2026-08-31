from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

from musician.views import MusicianViewSet

app_name = "musician"

router = SimpleRouter()
router.register("manage", MusicianViewSet, basename="manage")

urlpatterns = [path("", include(router.urls))]
