from models.models import MovieDatabaseManagement

movie_manager = MovieDatabaseManagement() 

def exit_program():
    print("Sad to see you leave! \U0001F61E")
    exit()

def display_all_movies():
  movies = movie_manager.get_all_movies()
  for movie in movies:
    print(f" => {movie.title}")
  print()

def display_movie():
  movie_id = input("Enter the movie's id: ")
  movie = movie_manager.display_movie_details(movie_id=movie_id)
  print(f" => {movie}")
  print()

def list_movie_by_genre():
  genre = input("Enter the movie's genre: ").title()
  movies = movie_manager.list_movies_by_genre(genre=genre)
  print(f" => {movies}")
  print()

def list_movie_by_release_year():
  year = input("Enter the year: ")
  movies = movie_manager.list_movies_by_release_year(release_year=year)
  for movie in movies:
    print(f" => {movie.title}")
  print()

def list_sorted_movies_by_rating():
  movies = movie_manager.sort_movies_by_rating()
  for movie in movies:
    print(f" => Title: {movie.title}, Rating: {movie.rating}")
  print()

def display_all_actors():
  actors = movie_manager.get_all_actors()
  for actor in actors:
    print(f" => Id: {actor.id}, Name: {actor.name}, Age: {actor.age}, Nationality: {actor.nationality} ")
  print()

def view_actors_in_movie():
  movie_id = input("Enter movie's id: ")
  actors = movie_manager.view_actors_in_movie(movie_id=movie_id)
  for actor in actors:
    print(f" => Id: {actor.id}, Name: {actor.name}, Age: {actor.age}, Nationality: {actor.nationality} ")
  print()

def view_movies_by_actors():
  actor_id = input("Enter actor's Id: ")
  movies = movie_manager.view_movies_by_actor(actor_id=actor_id)
  for movie in movies:
    print(f"=> Title: {movie.title}, Release Year: {movie.release_year}, Rating: {movie.rating}")
  print()

def display_all_directors():
  directors = movie_manager.get_all_directors()
  for director in directors:
    print(f" => Id: {director.id}, Name: {director.name}, Age: {director.age}, Nationality: {director.nationality} ")
  print()

def list_director_movies():
  dir_id = input("Enter the director's id: ")
  movies = movie_manager.view_directors_movies(director_id=dir_id)
  for movie in movies:
    print(f"=> Title: {movie.title}, Release Year: {movie.release_year}, Rating: {movie.rating}")
  print()
  
def remove_actor_from_movie():
  movie_id = input("Enter the movie's id: ")
  actor_id = input("Enter the actor's id: ")
  removed_movie = movie_manager.remove_actor_from_movie(movie_id=movie_id, actor_id=actor_id) 
  print(removed_movie)
  print()
  
def add_director():
  name = input("Enter the director's name: ").title()
  age = input("Enter the director's age: ")
  nationality = input("Enter the director's nationality: ").title()
  data = {"name": name, "age": age, "nationality": nationality}
  details = movie_manager.add_director(director_data=data)
  print(details)
  print()

def update_movie_data():
    movie_id = input("Enter the movie's id: ")
    
    updated_details = {}

    movie_title = input("Enter the movie's title (leave blank to keep current): ").title()
    if movie_title:
        updated_details["title"] = movie_title

    release_year = input("Enter the movie's release year (leave blank to keep current): ")
    if release_year:
        updated_details["release_year"] = release_year

    movie_genre = input("Enter the movie's genre (leave blank to keep current): ").title()
    if movie_genre:
        updated_details["genre"] = movie_genre

    movie_plot = input("Enter the movie's plot (leave blank to keep current): ")
    if movie_plot:
        updated_details["plot"] = movie_plot

    movie_rating = input("Enter the movie's rating (leave blank to keep current): ")
    if movie_rating:
        updated_details["rating"] = movie_rating

    movie_runtime = input("Enter the movie's runtime (leave blank to keep current): ")
    if movie_runtime:
        updated_details["runtime"] = movie_runtime

    movie_director_id = input("Enter the movie's director's id (leave blank to keep current): ")
    if movie_director_id:
        updated_details["director_id"] = movie_director_id

    details = movie_manager.update_movie_details(movie_id=movie_id, new_details=updated_details)
    print(details)
    print()

def add_movie():
    title = input("Enter the movie's title: ").title()
    release_year = input("Enter the movie's release year: ")
    genre = input("Enter the movie's genre: ").title()
    plot = input("Enter the movie's plot: ").strip
    rating = input("Enter the movie's rating (1-10): ")
    runtime = input("Enter the movie's runtime (in minutes): ")
    director_id = input("Enter the director's ID: ")

    # Create a dictionary with the movie details
    movie_data = {
        "title": title,
        "release_year": release_year,
        "genre": genre,
        "plot": plot,
        "rating": rating,
        "runtime": runtime,
        "director_id": director_id
    }
    movie = movie_manager.add_movie(movie_data)
    print(movie)

def list_top_movies():
  n = int(input("How many top movies would you like to view?: "))
  movies = movie_manager.list_top_n_movies(n)
  for movie in movies:
    print(f"=> {movie.title}, {movie.rating}, {movie.release_year}")
  print()

def delete_movie():
  movie_id = input("Enter the movie's id: ")
  deleted_movie = movie_manager.delete_movie(movie_id=movie_id)
  print(deleted_movie)
  print()

def search_actors():
  letter = input("Enter the beginning letter(s) of the actor's name: ")
  actors = movie_manager.search_actors_by_name_start(prefix=letter)
  for actor in actors:
    print(actor)
  print()

