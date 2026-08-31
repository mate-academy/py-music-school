from django.urls import include, path
from rest_framework import routers

from musician import views

router = routers.DefaultRouter()
router.register(r"musicians", views.MusicianViewSet, basename="manage")

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "musician"
