from django.urls import include, path
from rest_framework import routers

from musician.views import MusicianView

router = routers.DefaultRouter()
router.register("", MusicianView, basename="manage")


urlpatterns = [
    path("", include(router.urls))
]

app_name = "musician"
