from django.urls import path, include
from rest_framework import routers

from musician.views import MusicianView

router = routers.DefaultRouter()
router.register("musicians", MusicianView)

urlpatterns = [
    path("", include(router.urls))
]

app_name = "musician"
