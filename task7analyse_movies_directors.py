from task5movie_list_details import *

def analyse_movies_directors(movies_list):
    director =  get_movie_list_details(scrape_top_list)
    director_list = []
    for i in director:
        director_list.extend(i['director'])

    dict = {}
    for i in range(len(director_list)):
        count = 0
        for j in range(len(director_list)):
            if director_list[i] ==  director_list[j]:
                count=count+1
        dict[director_list[i]] = count
    return dict

pprint.pprint(analyse_movies_directors((get_movie_list_details(scrape_top_list))))

