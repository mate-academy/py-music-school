from django.urls import path

from musician import views

urlpatterns = [
    path(
        "musician/",
        views.MusicianListCreateView.as_view(),
        name="manage-list"),
    path(
        "musician/<int:pk>/",
        views.MusicianRetrieveUpdateDestroyView.as_view(),
        name="manage-detail")
]

app_name = "musician"
