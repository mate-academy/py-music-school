from rest_framework.routers import DefaultRouter
from django.urls import path, include
from musician.views import MusicianView

router = DefaultRouter()
router.register(r"manage", MusicianView, basename="manage")

urlpatterns = [
    path("", include(router.urls))
]

app_name = "musician"
