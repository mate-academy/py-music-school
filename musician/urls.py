from django.urls import path
from musician.views import (
    MusicianListCreateView,
    MusicianRetrieveUpdateDestroyView,
)


app_name = "musician"

urlpatterns = [
    path(
        "manage/",
        MusicianListCreateView.as_view(),
        name="manage-list"),
    path(
        "manage/<int:pk>/",
        MusicianRetrieveUpdateDestroyView.as_view(),
        name="manage-detail"),
]
