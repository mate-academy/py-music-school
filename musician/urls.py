from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ManageViewSet

router = DefaultRouter()
router.register(r"manage", ManageViewSet, basename="manage")

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "musician"
