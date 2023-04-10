from rest_framework import routers

from musician.views import MusicianView

router = routers.DefaultRouter()
router.register("musician", MusicianView, basename="manage")

urlpatterns = router.urls

app_name = "musician"
