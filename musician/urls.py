from django.urls import path
from musician.views import MusicianViewSet
from rest_framework import routers

app_name = "musician"

musician_list = MusicianViewSet.as_view(
    actions={
        "get": "list",
        "post": "create",
    }
)
musician_detail = MusicianViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)
router = routers.DefaultRouter()
router.register("musicians", MusicianViewSet)

urlpatterns = [
    path("musicians/", musician_list, name="manage-list"),
    path("musicians/<int:pk>/", musician_detail, name="manage-detail"),
]
