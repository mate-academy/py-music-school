from django.urls import path
from .views import MusicianViewSet


urlpatterns = [
    path("musicians/", MusicianViewSet.as_view(
        actions={
            "get": "list",
            "post": "create",
        }
    ), name="manage-list"),
    path("musicians/<int:pk>/", MusicianViewSet.as_view(
        actions={
            "get": "retrieve",
            "put": "update",
            "patch": "partial_update",
            "delete": "destroy",
        }
    ), name="manage-item"),
]

app_name = "musician"
