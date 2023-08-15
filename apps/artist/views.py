from rest_framework import viewsets
from django.http import JsonResponse
from django.views import View

from rest_framework import mixins
from rest_framework.response import Response

from apps.album.services import AlbumService
from apps.artist.service import ArtistService
from core.models.artist import Artist
from apps.artist.serializers import ArtistSerializer
from rest_framework import status


# Create your views here.
class ArtistViewSet(viewsets.ViewSet,
                    viewsets.GenericViewSet):
    queryset = Artist.nodes.all()
    serializer_class = ArtistSerializer
    lookup_field = 'id'
    service = ArtistService()

    def list(self, request, *args, **kwargs):
        queryset = Artist.nodes.all()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.service.get_or_404(id=self.kwargs[self.lookup_field])
        serializer = self.get_serializer(instance)
        return JsonResponse(serializer.data)

    def destroy(self, request, *args, **kwargs):
        self.service.delete_artist_by_id(id=self.kwargs[self.lookup_field])
        return Response(status=status.HTTP_204_NO_CONTENT)

    def create(self, request, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()
        response = self.service.create(validated_data=request.data).to_response()
        return JsonResponse(response, status=201)

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()
        response = self.service.update(id=self.kwargs[self.lookup_field], data=request.data).to_response()
        return JsonResponse(response, status=200)
