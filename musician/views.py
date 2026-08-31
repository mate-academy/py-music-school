from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from musician.models import Musician
from musician.serializers import MusicianSerializer, MusicianCreateSerializer


@api_view(["GET", "POST"])
def manage_list(request) -> Response:
    if request.method == "GET":
        musician = Musician.objects.all()
        serializer = MusicianSerializer(musician, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "POST":
        serializer = MusicianCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def musician_detail(request, pk) -> Response:
    musician = get_object_or_404(Musician, pk=pk)

    if request.method == "GET":
        serializer = MusicianSerializer(musician)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "PUT":
        serializer = MusicianCreateSerializer(musician, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "PATCH":
        serializer = MusicianCreateSerializer(
            musician,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "DELETE":
        musician.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
