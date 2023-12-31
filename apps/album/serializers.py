from rest_framework import serializers
from core.models.album import Album


class AlbumSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    title = serializers.CharField(required=True)
    release_year = serializers.IntegerField(required=True)
    belongs_to = serializers.CharField(required=True)

    # has_genre = serializers.StringRelatedField(read_only=True, many=True, required=False)  # Esto asumirá que el modelo Genre tiene un método __str__
    # liked_by = serializers.StringRelatedField(read_only=True, many=True, required=False)
    # listened_by = serializers.StringRelatedField(read_only=True, many=True, required=False)
    def to_representation(self, instance):
        return instance.to_response()

    def create(self, validated_data):
        album = Album(**validated_data)
        album.check_and_save()
        return album.to_response()
