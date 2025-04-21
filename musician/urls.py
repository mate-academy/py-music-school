from django.urls import include, path
from rest_framework.routers import DefaultRouter
from musician.views import MusicianViewSet


router = DefaultRouter()
router.register("musician", MusicianViewSet, basename="manage")

urlpatterns = [
    path("musician", include(router.urls)),
]

app_name = "musician"
