from django.urls import path, include
from rest_framework import routers

from musician.views import MusicianViewSet

musician_router = routers.DefaultRouter()

musician_router.register("musicians", MusicianViewSet, basename="manage")

urlpatterns = [path("", include(musician_router.urls)),]

app_name = "musician"
