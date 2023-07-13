from django.urls import include, path
from rest_framework import routers

from musician.views import MusicianViewSet

router = routers.DefaultRouter()
router.register("musician", MusicianViewSet)

musician_list = MusicianViewSet.as_view(actions={
    "get": "list",
    "post": "create",

})

urlpatterns = [
    path("", include(router.urls), name="manage-list"),
    path("musician/", musician_list, name="manage-list")
]

app_name = "musician"
