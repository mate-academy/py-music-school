from rest_framework import routers

from .views import MusicianViewsSet

router = routers.DefaultRouter()
router.register("musicians", MusicianViewsSet, basename="manage")
urlpatterns = [] + router.urls

app_name = "musician"
