from neomodel import (
    StructuredNode,
    StringProperty,
    IntegerProperty,
    RelationshipTo,
    RelationshipFrom,
    UniqueIdProperty,
)
from neomodel import config
import os

config.DATABASE_URL = os.getenv('NEO4J_DB_URL')

class Artist(StructuredNode):
    id = UniqueIdProperty()
    name = StringProperty(unique_index=True, required=True)

    # Relationships
    albums = RelationshipFrom('Album', 'BELONGS_TO')
    followed_by = RelationshipFrom('User', 'FOLLOWS')
