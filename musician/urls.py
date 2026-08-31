from rest_framework import routers
from musician.views import MusicianViewSet
from django.urls import path, include

app_name = "musician"
router = routers.DefaultRouter()
router.register(
    "musician",
    MusicianViewSet,
    basename="manage")
urlpatterns = [path("", include(router.urls))]
