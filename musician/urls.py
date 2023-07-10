from rest_framework import routers

from .views import MusicianViewSet

router = routers.DefaultRouter()
router.register("musicians", MusicianViewSet, basename="manage")

urlpatterns = [

              ] + router.urls

app_name = "musician"
