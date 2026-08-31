from rest_framework import routers
from musician.views import MusicianViewSet
from django.urls import path, include


router = routers.DefaultRouter()
router.register("musicians", MusicianViewSet, basename="manage")

urlpatterns = [path("", include(router.urls))]

app_name = "musician"
