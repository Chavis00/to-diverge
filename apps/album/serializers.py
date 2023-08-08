from rest_framework import serializers
from core.models.album import Album


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'
