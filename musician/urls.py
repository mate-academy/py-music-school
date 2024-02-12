from rest_framework import routers

from musician.views import MusicianViewSets

routers = routers.DefaultRouter()
routers.register("manage-list", MusicianViewSets, basename="manage")

urlpatterns = routers.urls

app_name = "musician"
