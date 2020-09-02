from task5movie_list_details import *

def analyse_movies_genre(movies_list):
    genre =  get_movie_list_details(scrape_top_list)
    genre_list = []
    for i in genre:
        genre_list.extend(i['genre'])
    # print(genre_list)

    dict = {}
    for i in range(len(genre_list)):
        count = 0
        for j in range(len(genre_list)):
            if genre_list[i] ==  genre_list[j]:
                count=count+1
        dict[genre_list[i]] = count
    # pprint.pprint(dict)
    return dict

pprint.pprint(analyse_movies_genre((get_movie_list_details(scrape_top_list))))