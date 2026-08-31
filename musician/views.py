from rest_framework import viewsets, mixins

from musician.models import Musician
from musician.serializers import MusicianSerializer


class MusicantView(viewsets.ModelViewSet):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer


class MusicantDetailView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer
