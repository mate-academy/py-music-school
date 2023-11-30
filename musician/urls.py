from django.urls import include, path
from rest_framework import routers

from musician.view import MusicianViewSet


router = routers.DefaultRouter()
router.register("musician", MusicianViewSet, basename="manage")


urlpatterns = [
    path("", include(router.urls))
]


app_name = "musician"
