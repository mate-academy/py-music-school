from rest_framework.viewsets import ModelViewSet

from musician.models import Musician
from musician.serializers import MusicianSerializer, MusicianDetailSerializer


class MusicianViewSet(ModelViewSet):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return MusicianDetailSerializer

        return MusicianSerializer
