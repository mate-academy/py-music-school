from django.urls import path, include

from rest_framework import routers

from musician.views import MusicantView

router = routers.DefaultRouter()
router.register("musician", MusicantView)

manage_list = MusicantView.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)


urlpatterns = [
    path("", include(router.urls)),
    path("musician/", manage_list, name="manage-list")
]

app_name = "musician"
