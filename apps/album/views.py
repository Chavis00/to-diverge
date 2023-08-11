from rest_framework import viewsets
from django.http import JsonResponse
from django.views import View

from rest_framework import mixins
from apps.album.exceptions import AlbumNotFoundException, CheckSentDataException
from apps.album.services import AlbumService
from core.models.album import Album
from apps.album.serializers import AlbumSerializer
from rest_framework import status
from rest_framework.response import Response


class AlbumViewSet(mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = Album.nodes.all()
    serializer_class = AlbumSerializer
    lookup_field = 'id'
    service = AlbumService()

    def retrieve(self, request, *args, **kwargs):
        instance = self.service.get_or_404(id=self.kwargs[self.lookup_field])
        serializer = self.get_serializer(instance)
        return JsonResponse(serializer.data)

    def destroy(self, request, *args, **kwargs):
        self.service.delete_album_by_id(id=self.kwargs[self.lookup_field])
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
