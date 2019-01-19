def import_file(filename):
    all_movies = {}
    with open(filename, "r") as f:
        lines = f.readlines()
        movie_title = ""
        for line in lines:
            if "[" in line:
                line = line.strip("\n").strip('[]')
                movie_title = line
                movie = {}
                all_movies.update({movie_title: movie})
            else:
                line = line.strip("\n").split("=")
                if line != [""]:
                    movie[line[0]] = line[1]
        return all_movies

print(import_file('film_data.ini'))

'''
def read_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    #movies = []
    #lst = []
    #for element in lines:
    #    if "[" in element:
    #        movies.append(lst)
    #        lst = []
    #    else:
    #        lst.append(element.replace("\n", "").split("="))

    movies = dict()
    dicti = dict()
    counter = -1
    movie_names = []
    for element in lines:
        if "[" in element:
            counter += 1
            movie_names.append(element)
            movies.update({counter: dicti})
            dicti = dict()
        else:
            sample = (element.replace("\n", "").split("="))
            for x in sample:
                if len(x) > 0:
                    #print(sample[0])
                    #input()
                    dicti.update({sample[0]: sample[1]})
    counter += 1
    movies.update({counter: dicti})
    movies.pop(0, None)

    return movies

    '''
            
def export_file(filename, all_movies):
    with open("film_data.ini", "w") as file:
        for k, v in all_movies.items():
            file.write("\n")
            title = k
            file.write("[" + title + "]" + "\n")
            for key, value in all_movies.items():
                row = key + "=" + value
                file.write(row + "\n")
		if 'genre' in row:
		    file.write("\n")
        
        
        
        
        
