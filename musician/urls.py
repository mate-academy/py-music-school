from django.urls import path

from musician.serializers import MusicianViewSet

urlpatterns = [
    path(
        "musicians/",
        MusicianViewSet.as_view(
            {"get": "list", "post": "create"}
        ),
        name="manage-list"
    ),
    path(
        "musicians/<int:pk>/",
        MusicianViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="musician-detail"
    ),
]

app_name = "musician"
