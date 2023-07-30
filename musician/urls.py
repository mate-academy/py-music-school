from django.urls import path

from musician.views import MusicianViewSet


manage_list = MusicianViewSet.as_view(actions={
    "get": "list",
    "post": "create"
})
manage_detail = MusicianViewSet.as_view(actions={
    "delete": "destroy",
    "put": "update",
    "patch": "partial_update",
    "get": "retrieve"
})

urlpatterns = [
    path("musicians/", manage_list, name="manage-list"),
    path("musicians/<int:pk>/", manage_detail, name="manage-detail")
]

app_name = "musician"
