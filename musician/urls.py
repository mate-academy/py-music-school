from rest_framework import routers

from musician.view import MusicianViewSet

routers = routers.DefaultRouter()
routers.register("musician", MusicianViewSet, basename="manage")

urlpatterns = routers.urls

app_name = "musician"
