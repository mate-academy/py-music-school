from rest_framework import routers
from django.urls import path, include
from .views import MusicianViewSet

router = routers.DefaultRouter()
router.register("musicians", MusicianViewSet, basename="manage")

urlpatterns = [
    path("", include(router.urls), name="list")
]

app_name = "musician"
