from rest_framework import mixins, viewsets

from musician.models import Musician
from musician.serializers import MusicianSerializer


class MusicianViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer
