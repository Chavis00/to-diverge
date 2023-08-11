from rest_framework import serializers
from core.models.album import Album


class AlbumSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    title = serializers.CharField(required=True)
    release_year = serializers.IntegerField(required=True)

    # belongs_to = serializers.StringRelatedField(read_only=True, required=False)  # Esto asumirá que el modelo Artist tiene un método __str__
    # has_genre = serializers.StringRelatedField(read_only=True, many=True, required=False)  # Esto asumirá que el modelo Genre tiene un método __str__
    # liked_by = serializers.StringRelatedField(read_only=True, many=True, required=False)
    # listened_by = serializers.StringRelatedField(read_only=True, many=True, required=False)

    def create(self, validated_data):
        album = Album(**validated_data)
        album.check_and_save()
        return album.to_response()
