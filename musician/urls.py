from rest_framework import routers
from django.urls import include, path

from musician.views import MusicianViewSet

routers = routers.DefaultRouter()
routers.register("musicians", MusicianViewSet, basename="manage")

urlpatterns = [path("", include(routers.urls))]

app_name = "musician"
