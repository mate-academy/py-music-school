from django.urls import include, path
from rest_framework.routers import DefaultRouter

from musician.views import MusicianViewSet

routers = DefaultRouter()
routers.register("musicians", MusicianViewSet, "manage")


urlpatterns = [
    path("", include(routers.urls))
]

app_name = "musician"
