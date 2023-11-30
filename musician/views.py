from rest_framework import viewsets


from .models import Musician
from .serializers import MusicianSerializer


class MusicianViewSet(viewsets.ModelViewSet):
    serializer_class = MusicianSerializer
    queryset = Musician.objects.all()
