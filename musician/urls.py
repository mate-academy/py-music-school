
from django.urls import include, path
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
# router = routers.DefaultRouter()
# router.register("musicians", MusicianViewSet)
#
# urlpatterns = [
#     path("", include(router.urls))
# ]

app_name = "musician"
