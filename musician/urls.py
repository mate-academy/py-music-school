from django.urls import path, include
from rest_framework import routers

from musician import views

router = routers.DefaultRouter()
router.register(r"musician", views.MusicianViewSet, basename="manage")

urlpatterns = [
    path("", include(router.urls)),
]


app_name = "musician"
