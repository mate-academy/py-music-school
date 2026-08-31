from django.urls import path

from musician.views import (MusicianListCreateView,
                            MusicianRetrieveUpdateDestroyView)

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

app_name = "musician"
