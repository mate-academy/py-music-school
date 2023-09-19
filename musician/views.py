from rest_framework import viewsets, status
from rest_framework.response import Response

from musician.models import Musician
from musician.serializers import MusicianSerializer


class MusicianViewSet(viewsets.ModelViewSet):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer

    def create(self, request, *args, **kwargs):
        age = request.data.get("age")
        if age is not None and int(age) < 21:
            return Response({"error": "age > 21"},
                            status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)
