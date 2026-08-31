from django.urls import path, include
from rest_framework import routers

from musician.views import MusicianSerializerViewSet

router = routers.DefaultRouter()
router.register("musicians", MusicianSerializerViewSet, basename="manage")

urlpatterns = [
    path("", include(router.urls))
]

app_name = "musician"
