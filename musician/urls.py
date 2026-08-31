from rest_framework.routers import DefaultRouter
from .views import MusicianViewSet

router = DefaultRouter()
router.register(r"manage", MusicianViewSet, basename="manage")
urlpatterns = router.urls
app_name = "musician"
