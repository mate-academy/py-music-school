from django.urls import path

from musician.views import MusicianViewSet

musician_list = MusicianViewSet.as_view(
    {"get": "list", "post": "create"})

musician_detail = MusicianViewSet.as_view(
    {
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    })

urlpatterns = [
    path("", musician_list, name="manage-list"),
    path("<int:pk>/", musician_detail, name="musician-detail")
]

app_name = "musician"
