from django.urls import path

from musician.views import MusicianListCreateView, MusicianDetailView

urlpatterns = [
    path(
        "musicians/",
        MusicianListCreateView.as_view(),
        name="manage-list"
    ),
    path(
        "musicians/<int:pk>/",
        MusicianDetailView.as_view(),
        name="manage-detail"
    ),
]

app_name = "musician"
