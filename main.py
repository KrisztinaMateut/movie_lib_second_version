import display
import statistics
import file_link
import data
import sys


def delete_movie(all_movies, selected_movie):

    if selected_movie in all_movies.keys():
        del all_movies[selected_movie]
    
    file_link.export_file(all_movies,'film_data.ini')

    return all_movies
    

def add_new_item(all_movies, movie_labels, inputs, user_input_title):

    inner_dict = {}
    for i in range(len(movie_labels)):
        inner_dict.update({movie_labels[i]: inputs[i]})

    all_movies.update({user_input_title: inner_dict})


    file_link.export_file(all_movies, 'film_data.ini')
    
    return all_movies


def show_added_item(movie_labels, inputs, user_input_title):

    inner_dict = {}
    for i in range(len(movie_labels)):
        inner_dict.update({movie_labels[i]: inputs[i]})

    addition = {}
    addition.update({user_input_title: inner_dict})

    return addition


def main():
    all_movies = file_link.import_file("film_data.ini")

    options = ["Display longest movie", 
                "Display shortest movie", 
                "Display the movie with the highest revenue",
                "Display movie by year", 
                "Display movie by star", 
                "Display movie by director",
                "Display total movie length",
                "Display average movie length",
                "Display movie closest to the average length",
                "Display year stats",
                "Display movies by genre",
                "Display last oldest",
                "Display last oldest of genre",
                "Display first youngest",
                "Display first youngest of genre",
                "Delete movie",
                "Add movie",
                "Show movies",
                "Export",
                "Exit"
                ]
    while True:
        print("          MAIN MENU" + "\n")
        display.print_options(options)
        try:
            option = input("Please enter a number: ")
            if option == "1":
                longests = statistics.get_longest_movie(all_movies)
                print("\n")
                print("The longest movie is: ")
                display.show_movie(longests)
                print("\n")
                input("Press ENTER to continue!")

            if option == "2":
                shortests = statistics.get_shortest_movie(all_movies)
                print("The shortest movie is: ")
                display.show_movie(shortests)
                print("\n")
                input("Press ENTER to continue!")
               
            if option == "3":
                highest_revenue = statistics.get_movie_of_highest_revenue(all_movies)
                print("The movie with the highest_revenue is: ")
                display.show_movie(highest_revenue)
                print("\n")
                input("Press ENTER to continue!")
                
            if option == "4":
                year = input("Please enter a year: ")
                movies_this_year = statistics.get_movie_by_year(all_movies, year)
                if movies_this_year is None:
                    print("There is no movie from this year")
                else:
                    print("The movies from this year are:")
                    display.show_movie(movies_this_year)
                print("\n")
                input("Press ENTER to continue!")
            
            if option == "5":
                star = input("Please enter a star: ")
                movies_this_star = statistics.get_movie_by_star(all_movies, star)
                if movies_this_star is None:
                    print("There is no movie with this star")
                else:
                    print("The movies with this star are:")
                    display.show_movie(movies_this_star)
                print("\n")
                input("Press ENTER to continue!")
               
            if option == "6":
                director = input("Please enter a director: ")
                movies_this_director = statistics.get_movie_by_director(all_movies, director)
                if movies_this_director is None:
                    print("There is no movie with this director")
                else:
                    print("The movies with this director are:")
                    display.show_movie(movies_this_director)
                print("\n")
                input("Press ENTER to continue!")

            if option == "7":
                total = statistics.get_total_movie_length(all_movies)
                print("The total length in minutes is: " + str(total))
                print("\n")
                input("Press ENTER to continue!")

            if option == "8":
                avg = statistics.get_average_movie_length(all_movies)
                print("The average length in minutes is: " + str(avg))
                print("\n")
                input("Press ENTER to continue!")
            
            if option == "9":
                closest = statistics.get_closest_to_average_length(all_movies)
                print("The movie closest to the average length is: ")
                display.show_movie(closest)
                print("\n")
                input("Press ENTER to continue!")

            if option == "10":
                year_stats = statistics.get_years_stats(all_movies)
                print("Year Stats: " + str(year_stats))
                print("\n")
                input("Press ENTER to continue!")
            
            if option == "11":
                genre = input("Please enter a genre: ")
                filtered_by_genre = statistics.get_movie_by_genre(all_movies, genre)
                if filtered_by_genre is None:
                    print("There are no movies of this genre")
                else:
                    print("The movies of this genre are: ")
                    display.show_movie(filtered_by_genre)
                print("\n")
                input("Press ENTER to continue!")
                
            if option == "12":
                last_oldest = statistics.get_last_oldest(all_movies)
                print("The last oldest movie is: ")
                display.show_movie(last_oldest)
                print("\n")
                input("Press ENTER to continue!")

            if option == "13": 
                genre = input("Please enter a genre: ")
                last_oldest_of_genre = statistics.get_last_oldest_of_genre(all_movies, genre)
                if last_oldest_of_genre is None:
                    print("There are no movies of this genre")
                else:
                    print("The last oldest movie of this genre is:  ")
                    display.show_movie(last_oldest_of_genre)
                print("\n")
                input("Press ENTER to continue!")

            if option == "14": 
                first_youngest = statistics.get_first_youngest(all_movies)
                print("The first youngest movie is: ")
                display.show_movie(first_youngest)
                print("\n")
                input("Press ENTER to continue!")

            if option == "15": 
                genre = input("Please enter a genre: ")
                first_youngest_of_genre = statistics.get_first_youngest_of_genre(all_movies, genre)
                if first_youngest_of_genre is None:
                    print("There are no movies of this genre")
                else:
                    print("The first youngest movie of this genre is: ")
                    display.show_movie(first_youngest_of_genre)
                print("\n")
                input("Press ENTER to continue!")

            if option == "16":
                movie_titles = ['Legends of the Fall',
                                'The Dressmaker',
                                'Brimstone',
                                'Blood Diamond',
                                'Water for Elephants',
                                'Queen of the Desert',
                                'Red Sparrow',
                                'The Kings Speech',
                                'Doctor Zhivago',
                                'A Beautiful Mind',
                                'Exit'
                                ]             
                display.print_options(movie_titles)
                selection = input("Please select an option to delete: ") 
                if int(selection) >= 1 and int(selection) <= 10:
                    selected = int(selection) - 1
                    for i in range(len(movie_titles)):
                        if i == selected:
                            selected_movie = movie_titles[i]
                    delete_movie(all_movies, selected_movie)
                elif int(selection) == 11:
                    break
                else:
                    print('This is not a valid option')
                    raise("KeyError")
                    input("Press ENTER to continue!")
            if option == "17":
                inputs = []
                print("Please fill in the following labels: ")
                user_input_title = input('title: ')
                movie_labels = ['director: ', 'stars: ', 'release_year: ', 'runtime: ', 'revenue: ', 'genre: ']
                for label in movie_labels:
                    user_input_other = input(label)
                    inputs.append(user_input_other)
                add_new_item(all_movies, movie_labels, inputs, user_input_title)
                print("\n")
                addition = show_added_item(movie_labels, inputs, user_input_title)
                print("The following movie was added: ")
                display.show_added_movie(addition)
                print("\n")
                input("Press ENTER to continue!") 
            if option == "18":
                display.show_movie(all_movies)
                print("\n")
                input("Press ENTER to continue!")              
            if option == "19":
                break
        except:
            print("This is not a valid option")
            print("\n")
            input("Press ENTER to continue!")


if __name__ == '__main__':
    main()



