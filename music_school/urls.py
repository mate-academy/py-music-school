from django.urls import path, include

urlpatterns = [
    path("api/", include(("musician.urls", "musician"), namespace="musician")),
]
