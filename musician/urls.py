from django.urls import path

from musician.view import MusicianViewSet

urlpatterns = [
    path("musicians/", MusicianViewSet.as_view(actions={
        "get": "list",
        "post": "create",
    }), name="manage-list"),
    path("musicians/<int:pk>/", MusicianViewSet.as_view(actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
    ), name="manage-detail"
    ),
]

app_name = "musician"
