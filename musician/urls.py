from django.urls import path
from .views import MusicianListCreate, MusicianDetail

urlpatterns = [
    path(
        "musicians/",
        MusicianListCreate.as_view(),
        name="manage-list"
    ),
    path(
        "musicians/<int:pk>/",
        MusicianDetail.as_view(),
        name="musician-detail"
    ),
]

app_name = "musician"
