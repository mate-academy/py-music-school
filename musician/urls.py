from django.urls import path, include
from rest_framework.routers import DefaultRouter

from musician.views import MusicianApiView

router = DefaultRouter()
router.register("musician", MusicianApiView, basename="manage")

urlpatterns = [
    path("", include(router.urls))
]

app_name = "musician"
