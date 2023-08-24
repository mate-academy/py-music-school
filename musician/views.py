from rest_framework import viewsets
from rest_framework.response import Response

from .models import Musician

from .serializers import MusicianSerializer


class MusicianViewSet(viewsets.ModelViewSet):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer
