from rest_framework import routers

from musician.views import MusicianViewSets

routers = routers.DefaultRouter()
routers.register("musicians", MusicianViewSets, basename="manage")

urlpatterns = routers.urls

app_name = "musician"
