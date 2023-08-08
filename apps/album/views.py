from rest_framework import viewsets
from django.http import JsonResponse
from django.views import View

from core.models.album import Album
from apps.album.serializers import AlbumSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


class AlbumView(viewsets.ModelViewSet):
    def create(self, request, *args, **kwargs):
        title = request.data['title']
        release_year = request.data['release_year']

        album = Album(title=title, release_year=release_year)
        print(album)
        album.save()

        response_data = {
            'id': str(album.id),
            'title': album.title,
            'release_year': album.release_year,
        }

        return JsonResponse(response_data, status=201)