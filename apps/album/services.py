from apps.album.exceptions import AlbumNotFoundException, AlbumAlreadyExistException
from apps.artist.service import ArtistService
from core.models.album import Album


class AlbumService:
    def __init__(self):
        self.model = Album
        self.artist_service = ArtistService()

    def get_or_404(self, id: str) -> Album:
        album = self.model.nodes.get_or_none(id=id)
        if album is None:
            raise AlbumNotFoundException(id)
        return album

    def delete(self, album: Album) -> None:
        self.model.delete(album)

    def delete_album_by_id(self, id: str) -> None:
        album = self.get_or_404(id=id)
        self.delete(album)

    def create(self, validated_data):
        title = validated_data['title']
        artist_id = validated_data['belongs_to']
        artist = self.artist_service.get_or_404(id=artist_id)
        if self.already_exist(title):
            raise AlbumAlreadyExistException(title)
        album = self.model(**validated_data)
        album.check_and_save()
        artist.albums.connect(album)
        artist.save()
        return album

    def update(self, id: str, data: dict) -> Album:
        album = self.get_or_404(id=id)
        album.update(data)
        album.check_and_save()
        return album

    def already_exist(self, title: str) -> bool:
        album = self.model.nodes.get_or_none(title=title)
        return album is not None
