from django.urls import path
from musician.views import MusicianViewSet

list_view = MusicianViewSet.as_view(
    actions={
        "get": "list",
        "post": "create"
    }
)

detail_view = MusicianViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)

urlpatterns = [
    path("musicians/", list_view, name="manage-list"),
    path("musicians/<int:pk>/", detail_view, name="manage-detail")
]

app_name = "musician"
