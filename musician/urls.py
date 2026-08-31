from django.urls import path, include

from musician.views import MusicianViewSet
from rest_framework.routers import DefaultRouter

app_name = "musician"
router = DefaultRouter()
router.register(
    r"musician/manage-list",
    MusicianViewSet,
    basename="manage")
urlpatterns = router.urls
