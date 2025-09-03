from rest_framework.routers import SimpleRouter

from musician.views import MusicianViewSet

router = SimpleRouter()
router.register(r"musicians", MusicianViewSet, basename="manage")

urlpatterns = router.urls

app_name = "musician"
