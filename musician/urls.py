from xml.etree.ElementInclude import include
from rest_framework import routers

from musician.views import MusicianViewSet
from django.urls import path, include

router = routers.SimpleRouter()
router.register(r"musicians", MusicianViewSet, basename="manage")

urlpatterns = [
    path("", include(router.urls))
]

app_name = "musician"
