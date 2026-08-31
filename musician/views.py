from rest_framework import viewsets

from .serializers import MusicianSerializer
from .models import Musician


class MusicianView(viewsets.ModelViewSet):
    serializer_class = MusicianSerializer
    queryset = Musician.objects.all()
