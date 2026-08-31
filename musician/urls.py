from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import MusicianViewSet

router = DefaultRouter()
router.register("manage", MusicianViewSet, basename="manage")

urlpatterns = [
    path("", include(router.urls))
]

app_name = "musician"
