from django.urls import path, include
from rest_framework import routers

from .views import MusicianView

router = routers.DefaultRouter()
router.register("musicians", MusicianView, basename="manage")

urlpatterns = [
    path("", include(router.urls), name="manage-list")
]

app_name = "musician"
