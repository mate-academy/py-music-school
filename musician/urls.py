from rest_framework import routers
from django.urls import path, include
from musician.views import MusicianSetView


router = routers.DefaultRouter()
router.register("musicians", MusicianSetView, basename="manage")

urlpatterns = [path("", include(router.urls))]

app_name = "musician"
