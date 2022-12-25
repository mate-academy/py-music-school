from django.urls import path

from musician.views import MusicianList, MusicianDetail

urlpatterns = [
    path("manage-list/", MusicianList.as_view(), name="manage-list"),
    path(
        "manage-list/<int:pk>/",
        MusicianDetail.as_view(),
        name="musician-detail"
    ),
]

app_name = "musician"
