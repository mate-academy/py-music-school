from django.urls import path

from musician.views import MusicianList, MusicianDetail

urlpatterns = [
    path("musicians/", MusicianList.as_view(), name="manage-list"),
    path(
        "musicians/<int:pk>/",
        MusicianDetail.as_view(),
        name="musician-detail"
    ),
]

app_name = "musician"
