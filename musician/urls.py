from rest_framework.routers import DefaultRouter
from .views import MusicianViewSet

app_name = "musician"

router = DefaultRouter()
router.register(r"manage", MusicianViewSet, basename="manage")

urlpatterns = router.urls
