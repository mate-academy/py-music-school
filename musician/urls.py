from django.urls import path
from rest_framework import routers

from musician.views import MusicianListViews

# router = routers.DefaultRouter()
#
# router.register("musicians", MusicianViews)

musician_list = MusicianListViews.as_view({"get": "list", "post": "create"})

musician_detail = MusicianListViews.as_view({
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy"
})

urlpatterns = [
    path("musicians/", musician_list, name="manage-list"),
    path("musicians/<int:pk>/", musician_detail, name="musician-detail")
]

app_name = "musician"
