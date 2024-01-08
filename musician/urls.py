from django.urls import include, path

from musician.views import MusicianViewSet

musician_list = MusicianViewSet.as_view(
    actions={"get": "list", "post": "create"}
)
musician_detail = MusicianViewSet.as_view(actions={
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy",
})


urlpatterns = [
    path("manage-list/", musician_list, name="manage-list"),
    path("manage-list/<int:pk>/", musician_detail, name="manage-detail"),
]

app_name = "musician"
