from django.template.context_processors import request
from rest_framework import viewsets
from rest_framework.response import Response

from musician.models import Musician
from musician.serializers import MusicianSerializer


class MusicianViewSet(viewsets.ModelViewSet):
    queryset = Musician.objects.all()

    serializer_class = MusicianSerializer
