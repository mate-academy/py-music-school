from rest_framework import routers
from django.urls import include, path

from musician.views import MusicianViewSet


router = routers.DefaultRouter()

router.register("musicians", MusicianViewSet)


urlpatterns = [
    path("", include(router.urls))
]

app_name = "musician"
