from rest_framework import routers

from django.urls import path, include

from musician.views import MusicianViewSet

router = routers.DefaultRouter()
router.register("manage-list", MusicianViewSet, basename="manage")

urlpatterns = [path("", include(router.urls))]

app_name = "musician"
