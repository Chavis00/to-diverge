from rest_framework import serializers

from apps.album.serializers import AlbumSerializer
from core.models.album import Album
from core.models.artist import Artist


class ArtistSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(required=True)

    # albums = AlbumSerializer(many=True, read_only=True)
    def to_representation(self, instance):
        representation = instance.to_response()
        return representation

    def create(self, validated_data):
        artist = Artist(**validated_data)
        artist.check_and_save()
        return artist.to_response()
