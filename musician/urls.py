from rest_framework import routers

from musician.view import MusicianViewSet


router = routers.SimpleRouter()
router.register("musicians", MusicianViewSet, basename="manage")

urlpatterns = router.urls

app_name = "musician"
