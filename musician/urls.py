from django.urls import include, path
from rest_framework import routers
from musician.views import MusicianViewSet


app_name = "musician"

urlpatterns = [
    path(
        "manage-list/",
        MusicianViewSet.as_view({"get": "list", "post": "create"}),
        name="manage-list",
    ),
    path(
        "manage-list/<int:pk>/",
        MusicianViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "delete": "destroy",
                "patch": "partial_update",
            }
        ),
        name="manage-detail",
    ),
]
