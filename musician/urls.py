from django.urls import path, include
from rest_framework.routers import DefaultRouter

from musician.views import MusicViewSet

router = DefaultRouter()
router.register("musician", MusicViewSet, basename="manage")

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "musician"
