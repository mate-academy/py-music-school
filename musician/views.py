from rest_framework.viewsets import ModelViewSet

from musician.serializers import MusicianSerializer

from musician.models import Musician


class MusicianSetView(ModelViewSet):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer
