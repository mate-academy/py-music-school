from rest_framework import generics

from musician.models import Musician
from musician.serializers import MusicianSerializer


class MusicianList(generics.ListCreateAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer


class MusicianDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer
