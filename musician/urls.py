from rest_framework.routers import DefaultRouter
from musician.views import MusicianViewSet

app_name = "musician"

router = DefaultRouter()
router.register("manage", MusicianViewSet, basename="manage")

urlpatterns = router.urls
