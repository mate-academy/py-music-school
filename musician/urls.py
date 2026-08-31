from rest_framework.routers import DefaultRouter
from django.urls import path, include
from musician.views import MusicianViewSet


app_name = "musician"

router = DefaultRouter()
router.register(r"musicians", MusicianViewSet, basename="manage")

urlpatterns = [
    path("", include(router.urls)),
]
