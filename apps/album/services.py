from apps.album.exceptions import AlbumNotFoundException
from core.models.album import Album


class AlbumService:
    def __init__(self):
        self.model = Album

    def get_or_404(self, id: str) -> Album:
        album = self.model.nodes.get_or_none(id=id)
        if album is None:
            raise AlbumNotFoundException()
        return album

    def delete(self, album: Album) -> None:
        self.model.delete(album)

    def delete_album_by_id(self, id: str) -> None:
        album = self.get_or_404(id=id)
        self.delete(album)

    def create(self, validated_data):
        album = self.model(**validated_data)
        album.check_and_save()
        return album

    def update(self, id: str, data: dict) -> Album:
        album = self.get_or_404(id=id)
        album.update(data)
        album.check_and_save()
        return album
