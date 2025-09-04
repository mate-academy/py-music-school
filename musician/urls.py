from django.urls import path

from musician.views import (
    MusicianListCreateView,
    MusicianRetrieveUpdateDestroyView
)


app_name = "musician"

urlpatterns = [
    path(
        "musicians/",
        MusicianListCreateView.as_view(),
        name="manage-list"
    ),
    path(
        "musicians/<int:pk>/",
        MusicianRetrieveUpdateDestroyView.as_view(),
        name="musician-detail"
    ),
]
