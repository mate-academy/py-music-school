from django.urls import include, path
from rest_framework.routers import DefaultRouter

from musician import views

router = DefaultRouter()
router.register("manage", views.MusicianViewSet, basename="manage")

urlpatterns = router.urls

app_name = "musician"
