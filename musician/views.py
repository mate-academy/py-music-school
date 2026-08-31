from rest_framework import viewsets
from musician.serializers import MusicianSerializer
from musician.models import Musician


class MusicianViewSet(viewsets.ModelViewSet):
    queryset = Musician.objects.all()

    def get_serializer_class(self) -> object:
        return MusicianSerializer
