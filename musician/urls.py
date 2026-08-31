from django.urls import path, include
from rest_framework.routers import DefaultRouter

from musician.views import MusicianViewSet, ManageListView

router = DefaultRouter()
router.register("musicians", MusicianViewSet, basename="musician")
router.register("manage", ManageListView, basename="manage")


urlpatterns = [
    path("", include(router.urls)),
]

app_name = "musician"
