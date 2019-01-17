import display
import statistics
import file_link
import data
import sys

def delete_movie(all_movies, selected_movie):

    if selected_movie in all_movies.keys():
        del all_movies[selected_movie]
            #all_movies.pop(key, None)
    
    file_link.export_file('film_data.ini', all_movies)

    return all_movies

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
                "Delete movie",
                "Exit"
                ]
    while True:

        print("          MAIN MENU" + "\n")
        display.print_options(options)
        try:
            option = input("Please enter a number: ")
            if option == "1":
                longests = statistics.get_longest_movie(all_movies)
                print("The longest movie is/are: " + str(longests))
                input("Press ENTER to continue!")

            if option == "2":
                shortests = statistics.get_shortest_movie(all_movies)
                print("The shortest movie is/are: " + str(shortests))
                input("Press ENTER to continue!")
               
            if option == "3":
                highest_revenue = statistics.get_movie_of_highest_revenue(all_movies)
                print("The movie with the highest_revenue is/are: " + str(highest_revenue))
                input("Press ENTER to continue!")
                
            if option == "4":
                year = input("Please enter a year: ")
                if statistics.get_movie_by_year(all_movies, year) is {}:
                    print("There is no movie from this year")
                else:
                    print(statistics.get_movie_by_year(all_movies, year))
                input("Press ENTER to continue!")
              
            if option == "5":
                star = input("Please enter a star: ")
                if statistics.get_movie_by_star(all_movies, star) is {}:
                    print("There is no movie with this star")
                else:
                    print(statistics.get_movie_by_star(all_movies, star))
                input("Press ENTER to continue!")
               
            if option == "6":
                director = input("Please enter a director: ")
                if statistics.get_movie_by_director(all_movies, director) is {}:
                    print("There is no movie with this director")
                else:
                    print(statistics.get_movie_by_director(all_movies, director))
                input("Press ENTER to continue!")

            if option == "7":
                total = statistics.get_total_movie_length(all_movies)
                print("The total length in minutes is: " + str(total))
                input("Press ENTER to continue!")

            if option == "8":
                avg = statistics.get_average_movie_length(all_movies)
                print("The total length in minutes is: " + str(avg))
                input("Press ENTER to continue!")
            
            if option == "9":
                closest = statistics.get_closest_to_average_length(all_movies)
                print("The movie closest to the average length is: " + str(closest))
                input("Press ENTER to continue!")

            if option == "10":
                year_stats = statistics.get_years_stats(all_movies)
                print("Year Stats: " + str(year_stats))
                input("Press ENTER to continue!")

            if option == "11":
                movie_titles = ['Legends of the Fall',
                                'The Dressmaker',
                                'Brimstone',
                                'Blood Diamond',
                                'Water for Elephants',
                                'Queen of the Desert',
                                'Red Sparrow',
                                'The Kings Speech',
                                'Doctor Zhivago',
                                'A Beautiful Mind'
                                ]
                display.print_options(movie_titles)
                try:
                    selection = input("Please select an option to delete: ")
                    #int(selection) >= 1 and int(selection) <= 10:
                    selected = int(selection) - 1
                    for i in range(len(movie_titles)):
                        if i == selected:
                            selected_movie = movie_titles[i]
                    print(delete_movie(all_movies, selected_movie))
                    input("Press ENTER to continue!")
                except:
                    print("KeyError")
                
            
            if option == "12":
                break
        except:
            print("KeyError")


if __name__ == '__main__':
    main()



