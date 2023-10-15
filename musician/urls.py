from rest_framework import routers as router
from django.urls import path, include

from musician.views import MusicianViewSet

router = router.DefaultRouter()
router.register("musicians", MusicianViewSet, basename="manage")

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "musician"
