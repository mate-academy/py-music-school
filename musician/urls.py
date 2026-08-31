from django.urls import path, include

from rest_framework import routers

from .views import MusicianViewSet

router = routers.DefaultRouter()
router.register("musician", MusicianViewSet, basename="manage")


urlpatterns = [
    path("", include(router.urls))
]

app_name = "musician"
