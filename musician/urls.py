from rest_framework import routers

from musician.view import MusicianViewSet


router = routers.DefaultRouter()
router.register(r"musicians", MusicianViewSet, "manage")


urlpatterns = router.urls

app_name = "musician"
