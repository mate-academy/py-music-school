from django.urls import include, path
from rest_framework import routers

from .views import MusicianViewSet

router = routers.DefaultRouter()
router.register("musicians", MusicianViewSet)

urlpatterns = [
    path("", include(router.urls))
]

app_name = "musician"
