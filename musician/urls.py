from django.urls import path
from rest_framework import routers

from musician import views


musician_list = views.MusicianViewSet.as_view(
    {
        "get": "list",
        "post": "create"
    }
)
musician_detail = views.MusicianViewSet.as_view(
    {
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy"
    }
)

urlpatterns = [
    path("musicians/", musician_list, name="manage-list"),
    path("musicians/<int:pk>/", musician_detail, name="manage-detail"),
]

app_name = "musician"
