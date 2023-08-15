from apps.album.exceptions import AlbumNotFoundException
from core.models.artist import Artist
from apps.artist.exceptions import ArtistNotFoundException, ArtistAlreadyExistException
from rest_framework import status


class ArtistService:
    def __init__(self):
        self.model = Artist

    def get_or_404(self, id: str) -> Artist:
        artist = self.model.nodes.get_or_none(id=id)
        if artist is None:
            raise ArtistNotFoundException(id)
        return artist

    def delete(self, artist: Artist) -> None:
        self.model.delete(artist)

    def delete_artist_by_id(self, id: str) -> None:
        artist = self.get_or_404(id=id)
        albums = artist.albums.all()
        for album in albums:
            album.delete()
        self.delete(artist)

    def create(self, validated_data):
        name = validated_data['name']
        if self.already_exist(name):
            raise ArtistAlreadyExistException(name)
        artist = self.model(**validated_data)

        artist.check_and_save()
        return artist

    def update(self, id: str, data: dict) -> Artist:
        album = self.get_or_404(id=id)
        album.update(data)
        album.check_and_save()
        return album

    def already_exist(self, name: str) -> bool:
        artist = self.model.nodes.get_or_none(name=name)
        return artist is not None
