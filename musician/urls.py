from django.urls import path, include
from rest_framework import routers

from musician.views import MusicianViewSet

router = routers.DefaultRouter()
router.register("musicians", MusicianViewSet, basename="manage")

urlpatterns = [
    path("manage-list", include(router.urls))
]

app_name = "musician"
