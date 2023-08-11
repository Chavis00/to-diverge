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

config.DATABASE_URL = os.getenv('NEO4J_DB_URL')

class Artist(DjangoNode):
    id = UniqueIdProperty()
    name = StringProperty(unique_index=True, required=True)

    # Relationships
    albums = RelationshipFrom('Album', 'BELONGS_TO')
    followed_by = RelationshipFrom('User', 'FOLLOWS')
    class Meta:
        app_label = 'core'
    def __str__(self):
        return self.name