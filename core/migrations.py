from neomodel import db, clear_neo4j_database
from core.models import User, album, artist, genre


def create_graph_indexes():
    # Create indexes for unique properties to improve query performance
    db.cypher_query(f"CREATE INDEX ON (n:{User}) ASSERT n.{User.id()} IS UNIQUE")
    db.cypher_query(f"CREATE INDEX ON (n:{Album}) ASSERT n.{Album.id()} IS UNIQUE")
    db.cypher_query(f"CREATE INDEX ON (n:{Artist}) ASSERT n.{Artist.id()} IS UNIQUE")
    db.cypher_query(f"CREATE INDEX ON (n:{Genre}) ASSERT n.{Genre.id()} IS UNIQUE")


def create_graph_data():
    # Your code to create or import data goes here
    pass


def run_migrations():
    # Clear the Neo4j database (Caution: This will delete all data in the database)
    clear_neo4j_database(db)

    # Create indexes
    create_graph_indexes()

    # Create or import data
    create_graph_data()


# Run the migrations
if __name__ == '__main__':
    run_migrations()
