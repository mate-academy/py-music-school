from django.urls import path

from musician.views import musician_list, musician_detail


urlpatterns = [
    path("musicians/", musician_list, name="manage-list"),
    path("musicians/<int:pk>/", musician_detail, name="musician_detail"),
]

app_name = "musician"
