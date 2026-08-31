from django.urls import include, path
from rest_framework.routers import SimpleRouter

from musician.views import MusicianViewSet

router = SimpleRouter()
router.register("musicians", MusicianViewSet, basename="manage")

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "musician"
