from django.urls import path

from musician.view import MusicianViewSet


musician_list = MusicianViewSet.as_view(actions={
    "get": "list",
    "post": "create",
})

musician_detail = MusicianViewSet.as_view(actions={
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy",
})

urlpatterns = [
    path("manage/", musician_list, name="manage-list"),
    path("manage/<int:pk>/", musician_detail, name="manage-detail")
]

app_name = "musician"
