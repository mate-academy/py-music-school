from django.urls import path, include

from musician.views import MusicianViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register("manage",
                MusicianViewSet,
                basename="manage")
urlpatterns = [
    path("", include(router.urls))
]

app_name = "musician"
