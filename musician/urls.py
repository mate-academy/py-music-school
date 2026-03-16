from django.urls import include, path
from rest_framework import routers

from musician.views import MusicianViewSet

router = routers.DefaultRouter()
router.register(r'musicians', MusicianViewSet , basename="manage")

app_name = 'musician'

urlpatterns = [
    path("", include(router.urls)),
]

