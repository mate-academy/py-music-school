from django.urls import path, include
from rest_framework import routers

from musician import views

app_name = "musician"

router = routers.DefaultRouter()
router.register(
    "manage",
    views.MusicianViewSet,
    basename="manage"
)
urlpatterns = [
    path("", include(router.urls)),
]
