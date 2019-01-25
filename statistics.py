
def get_movie_of_highest_revenue(all_movies):

    list_of_revenues = []

    for movie in all_movies.items():
        revenue = int(movie[1]['revenue'])
        list_of_revenues.append(revenue)

    list_of_revenues = sort_values_increasingly(list_of_revenues)

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

    if all_movies_with_this_year == {}:
        return None
    else:
        return all_movies_with_this_year


def get_movie_length(any_string):

    length = any_string.strip("min").split("h")
    converted_length = int(length[0]) * 60 + int(length[1])

    return converted_length


def get_lengths_converted_to_min(all_movies):

    list_of_lengths = []
    for movie in all_movies.items():
        time = get_movie_length(movie[1]['runtime'])
        list_of_lengths.append(time)

    return list_of_lengths


def sort_values_increasingly(any_list):

    length = len(any_list)

    for i in range(length-1):
        for j in range(1, length-i):
            if any_list[j-1] > any_list[j]:
                any_list[j-1], any_list[j] = any_list[j], any_list[j-1]

    return any_list


def get_longest_movie(all_movies):
    
    list_of_lengths = get_lengths_converted_to_min(all_movies)
    list_of_lengths = sort_values_increasingly(list_of_lengths)
    
    longests = {}

    for movie in all_movies.items():       
        if get_movie_length(movie[1]['runtime']) == list_of_lengths[-1]:
            longests.update({movie[0]: movie[1]})

    return longests


def get_shortest_movie(all_movies):

    list_of_lengths = get_lengths_converted_to_min(all_movies)
    list_of_lengths = sort_values_increasingly(list_of_lengths)

    shortests = {}

    for movie in all_movies.items():       
        if get_movie_length(movie[1]['runtime']) == list_of_lengths[0]:
            shortests.update({movie[0]: movie[1]})

    return shortests


def get_movie_by_director(all_movies, director):

    all_movies_with_this_director = {}
    for movie in all_movies.items():
        if director.lower() in (movie[1]['director']).lower():
            all_movies_with_this_director.update({movie[0]: movie[1]})

    if all_movies_with_this_director == {}:
        return None
    else:
        return all_movies_with_this_director


def get_movie_by_star(all_movies, star):

    all_movies_with_this_star = {}
    for movie in all_movies.items():
        if star.lower() in (movie[1]['stars']).lower():
            all_movies_with_this_star.update({movie[0]: movie[1]})

    if all_movies_with_this_star == {}:
        return None
    else:
        return all_movies_with_this_star
       

def sort_values_increasingly(any_list):

    length = len(any_list)

    for i in range(length-1):
        for j in range(1, length-i):
            if any_list[j-1] > any_list[j]:
                any_list[j-1], any_list[j] = any_list[j], any_list[j-1]

    return any_list

    
def get_distance_from_average(value, second_value):

    result = abs(value - second_value)
    result = round(result, 2)
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
    avg = round(avg, 2)

    return avg

def get_closest_to_average_length(all_movies):

    distance_from_avg = []
    avg = get_average_movie_length(all_movies)
    for movie in all_movies.items():
        item = get_distance_from_average(get_movie_length(movie[1]['runtime']), avg)
        distance_from_avg.append(item)
    
    distance_from_avg = sort_values_increasingly(distance_from_avg)

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


def get_years_list_increasingly(all_movies):

    years = []   
    for movie in all_movies.items():
        years.append(int(movie[1]['release_year']))

    years_sorted = sort_values_increasingly(years)

    return years_sorted


def get_last_oldest(all_movies):

    oldests = {}

    years = get_years_list_increasingly(all_movies)

    for movie in all_movies.items():
        if int(movie[1]['release_year']) == years[0]: 
            oldests.update({movie[0]: movie[1]})  

    results = []  
    for x in oldests.items(): 
        results.append(x)

    the_last_oldest = {} 
    
    the_last_oldest.update({results[-1][0]: results[-1][1]}) 
    
    return the_last_oldest


def get_movie_by_genre(all_movies, genre):
    
    filtered_by_genre = {}

    for movie in all_movies.items():
        if genre.lower() in (movie[1]['genre']).lower():
            filtered_by_genre.update({movie[0]: movie[1]})
    if len(filtered_by_genre) == 0:
        return None
    else:
        return filtered_by_genre
    
    
def get_last_oldest_of_genre(all_movies, genre):

    filtered_by_genre = get_movie_by_genre(all_movies, genre)

    if filtered_by_genre != None:
        last_oldest_of_genre = get_last_oldest(filtered_by_genre)
        return last_oldest_of_genre
    else:
        return None
    

def get_first_youngest(all_movies):

    youngests = {}

    years = get_years_list_increasingly(all_movies) 

    for movie in all_movies.items():
        if int(movie[1]['release_year']) == years[-1]: 
            youngests.update({movie[0]: movie[1]})  

    results = []  
    for x in youngests.items(): 
        results.append(x)

    the_first_youngest = {} 
    
    the_first_youngest.update({results[0][0]: results[0][1]}) 
    
    return the_first_youngest


def get_first_youngest_of_genre(all_movies, genre):

    filtered_by_genre = get_movie_by_genre(all_movies, genre)

    if filtered_by_genre != None:
       first_youngest_of_genre = get_first_youngest(filtered_by_genre)
       return first_youngest_of_genre
    else:
        return None
    

def split_and_reverse_name(any_name):
    
    splitted = any_name.split(' ')
    reversed = splitted[1], splitted[0]
    return reversed

def get_names_split_and_reversed(all_movies):

    first_name_last_name = []
    for movie in all_movies.items():
        first_name_last_name.append(split_and_reverse_name(movie[1]['director']))

    return first_name_last_name 


def sort_dictionary_by_directors_last_name_alphabetically(all_movies):

    first_name_last_name = get_names_split_and_reversed(all_movies)
    first_name_last_name = sort_values_increasingly(first_name_last_name)

    sorted_dict = {}

    tuples_list = []
    for movie in all_movies.items():
        content = split_and_reverse_name(movie[1]['director']), movie[0], movie[1]
        tuples_list.append(content)
        
    tuples_list = sort_values_increasingly(tuples_list)

    for item in tuples_list:
        sorted_dict.update({item[1]: item[2]})

    return sorted_dict






    
