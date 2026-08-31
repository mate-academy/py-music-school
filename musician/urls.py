from django.urls import path, include
from rest_framework import routers
from musician.views import MusicianViewSet


urlpatterns = [
    path("musicians/", MusicianViewSet.as_view(actions={
        "get": "list",
        "post": "create"
    }), name="manage-list"),
    path("musicians/<int:pk>/", MusicianViewSet.as_view(actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy"
    }), name="manage-item"),
]

app_name = "musician"
