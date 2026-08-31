from django.urls import path
from musician.views import MusicianViewSet


app_name = "musician"

musician_list = MusicianViewSet.as_view(
    actions={
        "get": "list",
        "post": "create"
    }
)
musician_detail = MusicianViewSet.as_view(
    {
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy"
    }
)

urlpatterns = [
    path("manage/", musician_list, name="manage-list"),
    path("manage/<int:pk>/", musician_detail, name="manage-detail"),
]
