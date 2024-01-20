from rest_framework.viewsets import ModelViewSet

from musician.models import Musician
from musician.serializers import MusicianSerializer, MusicianListSerializer, MusicianDetailSerializer


class MusicianViewSet(ModelViewSet):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return MusicianListSerializer
        if self.action == "retrieve":
            return MusicianDetailSerializer
        return MusicianSerializer

