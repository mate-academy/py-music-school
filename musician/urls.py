from django.urls import path, include

from rest_framework import routers

from musician.views import MusicianViewSet

router = routers.DefaultRouter()
router.register("musician", MusicianViewSet)

app_name = "musician"

urlpatterns = [
    path("", include(router.urls))
]
