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


class User(StructuredNode):
    id = UniqueIdProperty()
    username = StringProperty(unique_index=True, required=True)
    age = IntegerProperty()
    location = StringProperty()

    # Relationships
    listens_to = RelationshipTo('Album', 'LISTENS_TO')
    likes = RelationshipTo('Album', 'LIKES')
    follows_artist = RelationshipTo('Artist', 'FOLLOWS')
    follows_genre = RelationshipTo('Genre', 'FOLLOWS')
