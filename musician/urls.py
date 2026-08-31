from rest_framework import routers
from django.urls import path, include

from musician.views import MusicianViewSet

router = routers.DefaultRouter()
router.register("musicians", MusicianViewSet, basename="manage")

urlpatterns = [
    path("musican/", include(router.urls)),
]
app_name = "musician"
