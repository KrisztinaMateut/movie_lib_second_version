import file_link

all_movies = file_link.import_file('film_data.ini')



def get_movie_of_highest_revenue(all_movies):

    list_of_revenues = []

    for movie in all_movies.items():
        revenue = int(movie[1]['revenue'])
        list_of_revenues.append(revenue)

    list_of_revenues = sort_lengths_increasing(list_of_revenues)

    highest_revenue = {}

    for movie in all_movies.items():
        if int(movie[1]['revenue']) == list_of_revenues[-1]:
            highest_revenue.update({movie[0]: movie[1]})
    return highest_revenue



def get_movie_by_year(all_movies, year):

    all_movies_with_this_year = {}

    for movie in all_movies.items():
        if year in movie[1]['release_year']:
            all_movies_with_this_year.update({movie[0]: movie[1]})
            return all_movies_with_this_year



def get_movie_length(string):
    length = string.strip("min").split("h")
    converted_length = int(length[0]) * 60 + int(length[1])

    return converted_length

def get_lengths_converted_to_min(all_movies):

    list_of_lengths = []
    for movie in all_movies.items():
        time = get_movie_length(movie[1]['runtime'])
        list_of_lengths.append(time)

    return list_of_lengths



def sort_lengths_increasing(any_list):

    length = len(any_list)

    for i in range(length-1):
        for j in range(1, length-i):
            if any_list[j-1] > any_list[j]:
                any_list[j-1], any_list[j] = any_list[j], any_list[j-1]

    return any_list

def get_longest_movie(all_movies):
    
    list_of_lengths = get_lengths_converted_to_min(all_movies)
    list_of_lengths = sort_lengths_increasing(list_of_lengths)
    
    longests = {}

    for movie in all_movies.items():       
        if get_movie_length(movie[1]['runtime']) == list_of_lengths[-1]:
            longests.update({movie[0]: movie[1]})
    return longests


def get_shortest_movie(all_movies):

    list_of_lengths = get_lengths_converted_to_min(all_movies)
    list_of_lengths = sort_lengths_increasing(list_of_lengths)

    shortests = {}

    for movie in all_movies.items():       
        if get_movie_length(movie[1]['runtime']) == list_of_lengths[0]:
            shortests.update({movie[0]: movie[1]})
    return shortests


def get_movie_by_director(all_movies, director):
    all_movies_with_this_director = {}
    for movie in all_movies.items():
        if director in movie[1]['director']:
            all_movies_with_this_director.update({movie[0]: movie[1]})
    return all_movies_with_this_director


def get_movie_by_star(all_movies, star):
    all_movies_with_this_star = {}
    for movie in all_movies.items():
        if star in movie[1]['stars']:
            all_movies_with_this_star.update({movie[0]: movie[1]})
    return all_movies_with_this_star
       

# def add


# def get_last_oldest_of_genre
# def sort movie_by_number_of_stars


def sort_lengths_increasing(any_list):

    length = len(any_list)

    for i in range(length-1):
        for j in range(1, length-i):
            if any_list[j-1] > any_list[j]:
                any_list[j-1], any_list[j] = any_list[j], any_list[j-1]

    return any_list
    
def get_distance_from_average(value, second_value):
    result = abs(value - second_value)
    return result


def get_total_movie_length(all_movies):

    list_of_lengths = get_lengths_converted_to_min(all_movies)
    total = 0
    for item in list_of_lengths:
        total += item
    return total

def get_average_movie_length(all_movies):

    total = get_total_movie_length(all_movies)
    avg = total / len(all_movies)
    return avg

def get_closest_to_average_length(all_movies):
    distance_from_avg = []
    avg = get_average_movie_length(all_movies)
    for movie in all_movies.items():
        distance_from_avg.append(get_distance_from_average(get_movie_length(movie[1]['runtime']), avg))
    
    distance_from_avg = sort_lengths_increasing(distance_from_avg)

    closest = {}
    for movie in all_movies.items():
        if get_distance_from_average(get_movie_length(movie[1]['runtime']), avg) == distance_from_avg[0]:
            closest.update({movie[0]: movie[1]})
    return closest
        
def get_years_stats(all_movies):
    year_stats = {}
    for movie in all_movies.items():
        if movie[1]['release_year'] not in year_stats:
            year_stats.update({movie[1]['release_year']: 1})
        else:
            year_stats[movie[1]['release_year']] += 1
    return year_stats



def get_oldest(all_movies):

    oldests = {}

    years = []   
    for movie in all_movies.items():
        years.append(int(movie[1]['release_year']))

    years = sort_lengths_increasing(years)  #sort the list with years with bubble sort function

    for movie in all_movies.items():
        if int(movie[1]['release_year']) == years[0]: 
            oldests.update({movie[0]: movie[1]})  # gather the result/results into a dictionary

    results = []  
    for x in oldests.items(): #if there is more than one result append these to the result list as tuple: (movie title(outer dict) + movie details(inner dict)
        results.append(x)

    the_last_oldest = {} #make a final dict. which will contain only the one result
    
    the_last_oldest.update({results[-1][0]: results[-1][1]}) # 1st index represents the last tuple in results list, and the 2nd indexes are the indexes of the tuple: movie title and movie details

    return the_last_oldest




def get_youngest(all_movies):

    years = get_years_stats(all_movies)


    years_as_value = {}

    for year in years.items():
        years_as_value.update({year[1]: int(year[0])})
        
    return years_as_value


print(get_youngest(all_movies))





    