from neomodel import (
    StructuredNode,
    StringProperty,
    IntegerProperty,
    RelationshipTo,
    RelationshipFrom,
    UniqueIdProperty,
)
import os
from neomodel import config

config.DATABASE_URL = os.getenv('NEO4J_DB_URL')


class Genre(StructuredNode):
    id = UniqueIdProperty()
    name = StringProperty(unique_index=True, required=True)

    # Relationships
    albums = RelationshipFrom('Album', 'HAS_GENRE')
    followed_by = RelationshipFrom('User', 'FOLLOWS')
