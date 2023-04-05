from django.urls import path

from musician.views import manage_list, musician_detail

urlpatterns = [
    path("musician/", manage_list, name="manage-list"),
    path("musician/<int:pk>/", musician_detail, name="musician-detail"),

]

app_name = "musician"
