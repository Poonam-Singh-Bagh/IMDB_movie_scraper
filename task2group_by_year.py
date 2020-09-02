from task1top_movies import *
import pprint

def group_by_year(movie_list):
    year_list = []
    for movie in range(len(Top_movie_list)):
        if Top_movie_list[movie]['year'] not in year_list:
            year_list.append(Top_movie_list[movie]['year'])
    # print(year_list)

    dic= {}
    for i in range(len(year_list)):
        list = []
        for j in range(len(Top_movie_list)):
            if year_list[i] == Top_movie_list[j]['year']:
                list.append(Top_movie_list[j])
        dic[year_list[i]] = list
    return dic

# pprint.pprint(group_by_year(Top_movie_list))
year_group = group_by_year(Top_movie_list)
year_group
# pprint.pprint(year_group)