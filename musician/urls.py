from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MusicianViewSet

router = DefaultRouter()
router.register("musicians", MusicianViewSet, basename="manage")

urlpatterns = [
    path("music_school/", include(router.urls)),
]

app_name = "musician"
