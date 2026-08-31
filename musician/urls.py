from rest_framework import routers

from .views import MusicianViewSet


router = routers.SimpleRouter()
router.register(r"musicians", MusicianViewSet, basename="manage")

urlpatterns = router.urls

app_name = "musician"
