from django.urls import path, include
from rest_framework.routers import DefaultRouter
from musician.views import MusicianViewSet

router = DefaultRouter()
router.register(r"musicians", MusicianViewSet, basename="manage")

app_name = "musician"

urlpatterns = [
    path("", include(router.urls)),
]
