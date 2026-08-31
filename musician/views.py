from rest_framework.viewsets import ModelViewSet

from musician.models import Musician
from musician.serializers import MusicianSerializer


class MusicianViewSet(ModelViewSet):
    serializer_class = MusicianSerializer
    queryset = Musician.objects.all()
