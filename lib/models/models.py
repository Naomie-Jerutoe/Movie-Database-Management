from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import sessionmaker, relationship
import csv
import json
import os

engine = create_engine("sqlite:///movies.db")

Base = declarative_base()

class Movie(Base):
  __tablename__ = "movies"
  
  id = Column(Integer, primary_key=True, index=True)
  title = Column(String, index=True, nullable=False)
  release_year = Column(Integer, nullable=False)
  genre = Column(String, nullable=False)
  plot = Column(String, nullable=False)
  rating = Column(Integer, nullable=False)
  runtime = Column(Integer, nullable=False)
  director_id = Column(Integer, ForeignKey('directors.id'), nullable=False)
  
  director = relationship("Director", back_populates="movies")
  actors = relationship("Actor", secondary="movie_casts")
  
  def __repr__(self):
        return (
        f"<Movie(id={self.id}, title='{self.title}', "
        f"release_year={self.release_year}, genre='{self.genre}', "
        f"director_id={self.director_id})>"
    )

class Actor(Base):
  __tablename__ = "actors"
  
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, index=True, nullable=False)
  age = Column(Integer, nullable=False)
  nationality = Column(String, nullable=False)
    
  def __repr__(self):
        return (
          f"<Actor(id={self.id}, name='{self.name}', "
          f"age={self.age}, nationality='{self.nationality}')>")

class Director(Base):
  __tablename__ = "directors"
  
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, index=True, nullable=False)
  age = Column(Integer, nullable=False)
  nationality = Column(String, nullable=False)
  
  movies = relationship("Movie", back_populates="director")
  
  def __repr__(self):
        return (
          f"<Director(id={self.id}, name='{self.name}', "
          f"age={self.age}, nationality='{self.nationality}')>")

class MovieCast(Base):
    __tablename__ = "movie_casts"

    movie_id = Column(Integer, ForeignKey('movies.id'), primary_key=True, nullable=False)
    actor_id = Column(Integer, ForeignKey('actors.id'), primary_key=True, nullable=False)
    
    __table_args__ = (
        UniqueConstraint('actor_id', 'movie_id', name='_actor_movie_uc'),
    )
    
    def __repr__(self):
        return f"<MovieCast(movie_id={self.movie_id}, actor_id={self.actor_id})>"
      
class MovieDatabaseManagement:
  def __init__(self):
    Session = sessionmaker(bind=engine)
    self.session = Session()
  
  def get_all_movies(self):
    session = self.session
    return session.query(Movie).all()
  
  def display_movie_details(self, movie_id):
    session = self.session
    movie = session.query(Movie).filter_by(id=movie_id).first()
    if movie:
      return {
                "Title": movie.title,
                "Release Year": movie.release_year,
                "Genre": movie.genre,
                "Plot": movie.plot,
                "Rating": movie.rating,
                "Runtime": movie.runtime,
                "Director": movie.director.name,
                "Actors": [actor.name for actor in movie.actors]
            }
    return None
  
  def list_movies_by_genre(self, genre):
    session = self.session
    return session.query(Movie).filter_by(genre=genre).all()
  
  def list_movies_by_release_year(self, release_year):
    session = self.session
    return session.query(Movie).filter_by(release_year=release_year).all()
  
  def sort_movies_by_rating(self):
    session = self.session
    return session.query(Movie).order_by(Movie.rating.desc()).all()
  
  def get_all_actors(self):
    session =self.session
    return session.query(Actor).all()
  
  def view_actors_in_movie(self, movie_id):
    session = self.session
    movie = session.query(Movie).filter_by(id=movie_id).first()
    if movie:
      return movie.actors
    return []
  
  def view_movies_by_actor(self, actor_id):
    session = self.session
    movies = session.query(Movie).join(MovieCast).filter(MovieCast.actor_id == actor_id).all()
    if movies:
      return movies
    return []
  
  def get_all_directors(self):
    session =self.session
    return session.query(Director).all()
      
  def view_directors_movies(self, director_id):
    session = self.session
    director = session.query(Director).filter_by(id=director_id).first()
    if director:
        return director.movies
    return []
  
  def remove_actor_from_movie(self, movie_id, actor_id):
    session = self.session
    movie = session.query(Movie).filter_by(id=movie_id).first()
    if movie:
        actor = session.query(Actor).filter_by(id=actor_id).first()
        if actor in movie.actors:
            movie.actors.remove(actor)
            session.commit()
            return True
    return "Invalid details"

  def remove_director_from_movie(self, movie_id):
    session = self.session
    movie = session.query(Movie).filter_by(id=movie_id).first()
    if movie:
        movie.director = None
        session.commit()
        return True
    return False
  
  def add_director(self, director_data):
    session = self.session
    new_director = Director(**director_data)
    session.add(new_director)
    session.commit()
    return new_director
  
  def list_top_n_movies(self, n):
    session = self.session
    return session.query(Movie).order_by(Movie.rating.desc()).limit(n).all()
  
  def update_movie_details(self, movie_id, new_details):
    session = self.session
    movie = session.query(Movie).filter_by(id=movie_id).first()
    if movie:
      for key, value in new_details.items():
        if hasattr(movie, key):
          setattr(movie, key, value)
      session.commit()
      return "Movie Updated Successfully!"
    return "Failed to update movie details!"
  
  def add_movie(self, movie_data):
    session = self.session
    new_movie = Movie(**movie_data)
    session.add(new_movie)
    session.commit()
    return new_movie

  def delete_movie(self, movie_id):
        session = self.session
        movie = session.query(Movie).filter_by(id=movie_id).first()
        if movie:
            session.delete(movie)
            session.commit()
            return "Movie Deleted Successfully!"
        return "Failed to delete movie!"
  
  def search_actors_by_name_start(self, prefix):
        session = self.session
        actors = session.query(Actor).filter(Actor.name.like(f"{prefix}%")).all()
        return actors

  def export_movie_data(self, file_path, export_format):
        movies = self.get_all_movies()

        if export_format.lower() == 'csv':
            with open(file_path, 'w', newline='') as csvfile:
                fieldnames = ['Title', 'Release Year', 'Genre', 'Plot', 'Rating', 'Runtime', 'Director', 'Actors']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for movie in movies:
                    writer.writerow({
                        'Title': movie.title,
                        'Release Year': movie.release_year,
                        'Genre': movie.genre,
                        'Plot': movie.plot,
                        'Rating': movie.rating,
                        'Runtime': movie.runtime,
                        'Director': movie.director.name,
                        'Actors': ', '.join([actor.name for actor in movie.actors])
                    })
            return f"Movie data exported to {file_path} in CSV format."

        elif export_format.lower() == 'json':
            movie_list = []
            for movie in movies:
                movie_list.append({
                    'Title': movie.title,
                    'Release Year': movie.release_year,
                    'Genre': movie.genre,
                    'Plot': movie.plot,
                    'Rating': movie.rating,
                    'Runtime': movie.runtime,
                    'Director': movie.director.name,
                    'Actors': [actor.name for actor in movie.actors]
                })
            
            # # Ensure the directory exists before writing the file
            directory = os.path.dirname(file_path)
            if not os.path.exists(directory):
              os.makedirs(directory)

            with open(file_path, 'w') as jsonfile:
                json.dump(movie_list, jsonfile, indent=4)
            return f"Movie data exported to {file_path} in JSON format."
        else:
            return "Unsupported export format. Please specify either 'csv' or 'json'."