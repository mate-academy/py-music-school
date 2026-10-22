from django.urls import path, include

# from musician.views import MusicianViewSet

from musician.views import MusicianList, MusicianDetail

urlpatterns = [
    path("manage/", MusicianList.as_view(), name="manage-list"),
    path("manage/<int:pk>/", MusicianDetail.as_view(), name="manage-detail"),
]

# router = routers.DefaultRouter()
# router.register("musician", MusicianViewSet)
#
# urlpatterns = [
#     path("", include(router.urls), name="musician"),
# ]

app_name = "musician"
