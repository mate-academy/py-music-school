from musician.views import MusicianViewSet
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register("manage-list", MusicianViewSet, basename="manage")


urlpatterns = [
    path("musician/", include(router.urls)),
]

app_name = "musician"
