from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MusicianViewSet

router = DefaultRouter()
router.register(r"musicians", MusicianViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
