from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from musician.models import Musician
from musician.serializers import MusicianSerializer


class MusicianViewSet(viewsets.ModelViewSet):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer


class ManageListView(viewsets.ModelViewSet):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer

    @action(detail=True, methods=["get"])
    def is_adult(self, request):
        is_adult = self.get_object().age >= 21
        return Response({"is_adult": is_adult})

    def create(self, request, *args, **kwargs):
        if "age" in request.data and int(request.data["age"]) < 21:
            return Response(
                {"error": "Age must be 21 or above."},
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        self.perform_destroy(self.get_object())
        return Response(status=status.HTTP_204_NO_CONTENT)
