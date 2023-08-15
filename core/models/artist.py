from neomodel import (
    StructuredNode,
    StringProperty,
    IntegerProperty,
    RelationshipTo,
    RelationshipFrom,
    UniqueIdProperty,
)
from django_neomodel import DjangoNode

from neomodel import config
import os

from apps.artist.exceptions import CheckSentDataException

config.DATABASE_URL = os.getenv('NEO4J_DB_URL')


class Artist(DjangoNode):
    id = UniqueIdProperty()
    name = StringProperty(unique_index=True, required=True)

    # Relationships
    albums = RelationshipFrom('core.models.album.Album', 'BELONGS_TO')

    class Meta:
        app_label = 'core'

    def __str__(self):
        return self.name

    def to_response(self) -> dict:
        response = {
            'id': str(self.id),
            'name': self.name,
            'albums': [album.to_response() for album in self.albums.all()]
        }
        return response

    def check_and_save(self) -> None:
        self._check_album_attributes()
        self.save()

    def update(self, data: dict) -> None:
        self.__dict__.update(data)

    def _check_album_attributes(self) -> None:
        if not isinstance(self.name, str):
            raise CheckSentDataException()
        if 1 > len(self.name) > 190:
            raise CheckSentDataException()
