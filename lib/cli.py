from helpers import (
    exit_program,
    display_all_movies,
    display_movie,
    list_movie_by_genre,
    list_movie_by_release_year,
    list_sorted_movies_by_rating,
    display_all_actors,
    view_actors_in_movie,
    view_movies_by_actors,
    display_all_directors,
    list_director_movies,
    remove_actor_from_movie,
    add_director,
    update_movie_data,
    add_movie,
    list_top_movies,
    delete_movie,
    search_actors,
    export_movie_data
)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            display_all_movies()
        elif choice == "2":
            display_movie()
        elif choice == "3":
            list_movie_by_genre()
        elif choice == "4":
            list_movie_by_release_year()
        elif choice == "5":
            list_sorted_movies_by_rating()
        elif choice == "6":
            display_all_actors()
        elif choice == "7":
            view_actors_in_movie()
        elif choice == "8":
            view_movies_by_actors()
        elif choice == "9":
            display_all_directors()
        elif choice == "10":
            list_director_movies()
        elif choice == "11":
            remove_actor_from_movie()
        elif choice == "12":
            add_director()
        elif choice == "13":
            update_movie_data()
        elif choice == "14":
            add_movie()
        elif choice == "15":
            list_top_movies()
        elif choice == "16":
            delete_movie()
        elif choice == "17":
            search_actors()
        elif choice == "18":
            export_movie_data()
        else:
            print("Invalid Choice")

def menu():
    print("Please select an option: \U0001F60A")
    print("0. Exit the program")
    print("1. Display all movies")
    print("2. Display a movie")
    print("3. List movie by genre")
    print("4. List movie by release year")
    print("5. List movies by rating")
    print("6. Display all actors")
    print("7. List actors in a movie")
    print("8. List movies by an actor")
    print("9. Display all directors")
    print("10. View movies of a director")
    print("11. Remove actor from a movie")
    print("12. Add Director")
    print("13. Update Movie Details")
    print("14. Add Movie")
    print("15. View the top movies")
    print("16. Delete a movie")
    print("17. Search actor by first letter")
    print("18. Export movie data")

if __name__ == "__main__":
    main()