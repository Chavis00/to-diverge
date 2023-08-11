from neomodel import (
    StructuredNode,
    StringProperty,
    IntegerProperty,
    RelationshipTo,
    RelationshipFrom,
    UniqueIdProperty,
)
from django_neomodel import DjangoNode

import os
from neomodel import config

config.DATABASE_URL = os.getenv('NEO4J_DB_URL')


class Genre(DjangoNode):
    id = UniqueIdProperty()
    name = StringProperty(unique_index=True, required=True)

    # Relationships
    albums = RelationshipFrom('Album', 'HAS_GENRE')
    followed_by = RelationshipFrom('User', 'FOLLOWS')
    class Meta:
        app_label = 'core'

    def __str__(self):
        return self.name