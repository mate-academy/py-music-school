from rest_framework import routers

from musician.views import MusicianViewSet


app_name = "musician"

router = routers.DefaultRouter()
router.register("manage-list", MusicianViewSet, basename="manage")

urlpatterns = router.urls
