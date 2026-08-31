from django.urls import path
from musician.views import MusicianSetView


musician_list = MusicianSetView.as_view(
    actions={
        "get": "list",
        "post": "create"
    }
)

musician_detail = MusicianSetView.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy"
    }
)
urlpatterns = [
    path("musicians/", musician_list, name="manage-list"),
    path("musicians/<int:pk>/", musician_detail, name="manage-detail")
]

app_name = "musician"
