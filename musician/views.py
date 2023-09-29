from rest_framework import viewsets

from .serializers import (
    MusicianSerializer,
)
from .models import Musician


class MusicianViewSet(viewsets.ModelViewSet):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer
