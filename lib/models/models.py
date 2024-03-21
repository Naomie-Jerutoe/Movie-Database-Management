from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("sqlite:///movies.db")

Session = sessionmaker(bind=engine)

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
      
