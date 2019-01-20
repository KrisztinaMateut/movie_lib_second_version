def print_options(options):
    for option in options:
        print(str(options.index(option)+1) + '.\t' + option)

def print_movie_list(dicti):
    for key, value in dicti.items():
        print('{}: {}'.format(key, value))


def show_movie(any_dict):
    
    lengthKey = 0
    for key, value in any_dict.items():
        if len(key) > lengthKey:
            lengthKey = len(key)
    
    withSpace = " "
    for k, v in any_dict.items():
        print("\n")
        print(k)
        for x, y in v.items():
            print('{}: {} {}'.format(x, (withSpace * (lengthKey - len(x))), y))
  


