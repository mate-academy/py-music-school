from rest_framework import routers

from musician.views import MusiciansViewSet

route = routers.DefaultRouter()
route.register("musicians", MusiciansViewSet, basename="manage")

urlpatterns = route.urls

app_name = "musician"
