from task2group_by_year import *
import pprint

def group_by_decade(top_movie):
    decade_list = []
    for movie in year_list:
        year = movie//10
        decade = year*10
        decade_list.append(decade)
    decade_year_list = []
    for i in decade_list:
        if i not in decade_year_list:
            decade_year_list.append(i)
    decade_year_list.sort()   

    dictionary={}
    for movie_year in range(len(decade_year_list)):
        movie_decade_list = []
        # List = []
        for key in dic:
            print(key)
            dec = decade_year_list[movie_year] + 9
            if key >= decade_year_list[movie_year] and key <= dec:
                movie_decade_list.append(dic[key])
            # List.extend(movie_decade_list)
        dictionary[decade_year_list[movie_year]] = movie_decade_list
    # pprint.pprint(dictionary)
    return dictionary


pprint.pprint(group_by_decade(Top_movie_list))

