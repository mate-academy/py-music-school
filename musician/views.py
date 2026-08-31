from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Musician
from .serializers import MusicianSerializer


class MusicianViewSet(viewsets.ModelViewSet):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_fields = ["instrument", "age"]
    search_fields = ["first_name", "last_name", "instrument"]
    ordering_fields = ["age", "date_of_applying"]
