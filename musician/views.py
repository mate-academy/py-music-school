from rest_framework.viewsets import ModelViewSet
from .models import Musician
from .serializers import MusicianSerializer


class MusicianViewSet(ModelViewSet):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer
