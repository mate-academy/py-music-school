from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from musician.models import Musician
from musician.serializers import MusicianSerializer


class MusicianList(APIView):
    def get(self, request):
        musicians = Musician.objects.all()
        serializer = MusicianSerializer(musicians, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MusicianSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MusicianDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(Musician, pk=pk)

    def get(self, request, pk):
        musician = self.get_object(pk)
        serializer = MusicianSerializer(musician)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        musician = self.get_object(pk)
        serializer = MusicianSerializer(musician, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        musician = self.get_object(pk)
        serializer = MusicianSerializer(
            musician,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        musician = self.get_object(pk)
        musician.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
