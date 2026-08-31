from django.urls import path, include
from rest_framework.routers import DefaultRouter
from musician.views import MusicianViewSet

router = DefaultRouter()

router.register("musician", MusicianViewSet, basename="manage")

urlpatterns = [path("", include(router.urls), name="list")]

app_name = "musician"
