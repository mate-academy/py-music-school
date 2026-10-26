from rest_framework import routers
from django.urls import include, path
from musician.views import MusicianViewSets


app_name = "musician"

router = routers.DefaultRouter()
router.register("musician", MusicianViewSets, basename="manage")

urlpatterns = [
    path("", include(router.urls)),
]
