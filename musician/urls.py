from django.urls import path

from musician.views import MusicianViewSet

author_list = MusicianViewSet.as_view(actions={
    "get": "list",
    "post": "create"
})
author_detail = MusicianViewSet.as_view(actions={
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy"
})


urlpatterns = [
    path(
        "musicians/",
        author_list,
        name="manage-list"
    ),
    path(
        "musicians/<int:pk>/",
        author_detail,
        name="manage-detail"
    )
]


app_name = "musician"
