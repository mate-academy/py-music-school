from rest_framework import generics

from musician.models import Musician
from musician.serializers import MusicianSerializer


class MusicianListCreateView(generics.ListCreateAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer


class MusicianRetrieveUpdateDestroyView(
    generics.RetrieveUpdateDestroyAPIView
):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer
