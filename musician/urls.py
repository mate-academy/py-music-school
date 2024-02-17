from django.urls import path

from musician.views import MusicianViewSet

author_list = MusicianViewSet.as_view(
    actions={"get": "list", "post": "create"}
)

author_detail = MusicianViewSet.as_view(
    {
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)

urlpatterns = [
    path("musician/", author_list, name="manage-list"),
    path(
        "musician/<int:pk>/", author_detail, name="author-detail"
    ),
]

app_name = "musician"
