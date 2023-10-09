from .views import MusicianViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register("musicians", MusicianViewSet, basename="manage")

urlpatterns = router.urls

app_name = "musician"
