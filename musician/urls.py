from django.urls import path, include
from rest_framework import routers

from musician.views import MusicianViewSet

routers = routers.DefaultRouter()
routers.register("musicians", MusicianViewSet, basename="manage")

urlpatterns = [
    path("", include(routers.urls)),
]

app_name = "musician"
