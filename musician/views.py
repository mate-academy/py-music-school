from rest_framework import viewsets, permissions

from .models import Musician
from .serializers import MusicianSerializer


class MusicianViewSet(viewsets.ModelViewSet):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer
    permission_classes = [permissions.AllowAny]
