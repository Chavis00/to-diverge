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


class Album(StructuredNode):
    id = UniqueIdProperty()
    title = StringProperty(unique_index=True, required=True)
    release_year = IntegerProperty()

    # Relationships
    belongs_to = RelationshipTo('core.models.artist.Artist', 'BELONGS_TO')
    has_genre = RelationshipTo('core.models.genre.Genre', 'HAS_GENRE')
    liked_by = RelationshipFrom('core.models.user.User', 'LIKES')
    listened_by = RelationshipFrom('core.models.user.User', 'LISTENS_TO')
