from django.urls import path
from . import views

app_name = "musician"

urlpatterns = [
    path("musicians/", views.MusicianList.as_view(), name="musician-list"),
    path(
        "musicians/<int:pk>/",
        views.MusicianDetail.as_view(),
        name="musician-detail"
    ),
]
