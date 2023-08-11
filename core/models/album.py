from collections import OrderedDict

from neomodel import (
    StructuredNode,
    StringProperty,
    IntegerProperty,
    RelationshipTo,
    RelationshipFrom,
    UniqueIdProperty,
)
from django_neomodel import DjangoNode
from datetime import datetime

from neomodel import config
import os
from django.db import models
from apps.album.exceptions import AlbumAlreadyExistException, CheckSentDataException

config.DATABASE_URL = os.getenv('NEO4J_DB_URL')


class Album(DjangoNode):
    id = UniqueIdProperty()
    title = StringProperty(unique_index=True, required=True, max_length=190)
    release_year = IntegerProperty()

    # Relationships
    belongs_to = RelationshipTo('core.models.artist.Artist', 'BELONGS_TO')
    has_genre = RelationshipTo('core.models.genre.Genre', 'HAS_GENRE')
    liked_by = RelationshipFrom('core.models.user.User', 'LIKES')
    listened_by = RelationshipFrom('core.models.user.User', 'LISTENS_TO')

    class Meta:
        app_label = 'core'

    def __str__(self):
        return self.title

    def to_response(self) -> dict:

        response = {
            'id': str(self.id),
            'title': self.title,
            'release_year': self.release_year,
        }
        return response

    def check_and_save(self) -> None:
        self._check_album_attributes()
        self._check_if_album_already_exist()
        self.save()

    def update(self, data: dict) -> None:
        self.__dict__.update(data)

    def _check_if_album_already_exist(self) -> None:
        album_with_same_title = Album.nodes.get_or_none(title=self.title)
        if album_with_same_title and album_with_same_title != self:
            raise AlbumAlreadyExistException(self.title)

    def _check_album_attributes(self) -> None:
        if not isinstance(self.release_year, int) or (not isinstance(self.title, str)):
            raise CheckSentDataException()
        if len(self.title) > 190:
            raise CheckSentDataException()
        if self.release_year < 1900 or self.release_year > datetime.date(datetime.now()).today().year:
            raise CheckSentDataException()