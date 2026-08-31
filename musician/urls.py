from django.urls import path


from musician.views import MusicianViewSet

app_name = "musician"

musician_list = MusicianViewSet.as_view(actions={
    "get": "list",
    "post": "create"}
)
musician_detail = MusicianViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "delete": "destroy",
        "patch": "partial_update",
    }
)

urlpatterns = [
    path("musicians/", musician_list, name="manage-list"),
    path("musicians/<int:pk>/", musician_detail, name="manage-list"),
]
