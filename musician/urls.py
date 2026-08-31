from django.urls import path

from musician.views import MusicianViewSet

urlpatterns = [
    path(
        "manage-list/",
        MusicianViewSet.as_view({"get": "list", "post": "create"}),
        name="manage-list",
    ),
    path(
        "manage-list/<int:pk>/",
        MusicianViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="manage-list-detail",
    ),
]

app_name = "musician"
