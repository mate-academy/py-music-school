from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Musician
from .serializers import MusicianSerializer


@api_view(["GET", "POST"])
def musician_list(request):
    if request.method == "GET":
        musicians = Musician.objects.all()
        serializer = MusicianSerializer(musicians, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = MusicianSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def musician_detail(request, pk):
    musician = get_object_or_404(Musician, pk=pk)

    if request.method == "GET":
        serializer = MusicianSerializer(musician, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method in ["PUT", "PATCH"]:
        serializer = MusicianSerializer(musician, data=request.data, partial=request.method == "PATCH")
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "DELETE":
        musician.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
