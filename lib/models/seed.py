from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import configure_mappers
from models import (
    Base, engine, Session, Movie, Actor, Director, MovieCast
)

# Ensure all mappings are configured
configure_mappers()

# Create session
Session = sessionmaker(bind=engine)
session = Session()

def seed_database():
    # Create tables if they do not exist
    Base.metadata.create_all(engine)

    # Seed movies
    movie_data = [
        {
            "title": "The Giant Gila Monster",
            "release_year": 2010,
            "genre": "Fantasy",
            "plot": "A giant lizard terrorizes a rural Texas community and a heroic teenager attempts to destroy the creature.",
            "rating": 8,
            "runtime": 120,
            "director_id": 1
        },
        {
            "title": "Time Chasers",
            "release_year": 2015,
            "genre": "Science-fiction",
            "plot": "An inventor comes up with a time machine, but must prevent its abuse at the hands of an evil C.E.O.",
            "rating": 7,
            "runtime": 110,
            "director_id": 2
        },
        {
            "title": "Avatar The Last Air Bender",
            "release_year": 2024,
            "genre": "Fiction, Mystery",
            "plot": "Journey of twelve-year-old Aang, the current Avatar and last survivor of his nation, the Air Nomads, along with his friends Katara, Sokka, and Toph, as they strive to end the Fire Nation's war against the other nations and defeat Fire Lord Ozai before he conquers the world.",
            "rating": 9,
            "runtime": 420,
            "director_id": 3
        },
        {
            "title": "Secret Agent Super Dragon",
            "release_year": 2018,
            "genre": "Action",
            "plot": "A series of murders in Michigan lead an American secret agent to Amsterdam, where he uncovers a plot to imperil the world with a potent new drug.",
            "rating": 8,
            "runtime": 100,
            "director_id": 2
        }
    ]
    for movie_info in movie_data:
        movie = Movie(**movie_info)
        session.add(movie)

    # Seed actors
    actor_data = [
        {
            "name": "Morgan Freeman",
            "age": 49,
            "nationality": "USA"
        },
        {
            "name": "Sandra Bullock",
            "age": 35,
            "nationality": "UK"
        },
        {
            "name": "Jackie Chan",
            "age": 45,
            "nationality": "China"
        },
        {
            "name": "Lupitah Nyong'o",
            "age": 41,
            "nationality": "Kenya"
        }
    ]
    for actor_info in actor_data:
        actor = Actor(**actor_info)
        session.add(actor)

    # Seed directors
    director_data = [
        {
            "name": "Tyler Perry",
            "age": 54,
            "nationality": "USA"
        },
        {
            "name": "Johnson Doe",
            "age": 45,
            "nationality": "Rwanda"
        },
        {
            "name": "Jane Julius",
            "age": 35,
            "nationality": "Kenya"
        }
    ]
    for director_info in director_data:
        director = Director(**director_info)
        session.add(director)

    # Seed movie cast
    movie_cast_data = [
        {
            "movie_id": 1,  
            "actor_id": 1  
        },
        {
            "movie_id": 1,  
            "actor_id": 2 
        },
        {
            "movie_id": 1,  
            "actor_id": 3
        },
        {
            "movie_id": 2,  
            "actor_id": 2
        },
        {
            "movie_id": 3,  
            "actor_id": 1
        }
        
    ]
    for movie_cast_info in movie_cast_data:
        movie_cast = MovieCast(**movie_cast_info)
        session.add(movie_cast)

    # Commit changes
    session.commit()

if __name__ == "__main__":
    seed_database()
    print("Database seeded successfully.")
