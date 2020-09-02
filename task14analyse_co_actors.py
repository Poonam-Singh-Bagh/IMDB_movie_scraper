from task13scrape_movie_details import *
from task1top_movies import *
# from task12scrape_movie_cast import *

def analyse_co_actors(movies_list):
    cast_details = {}
    for cast in movies_list['cast'][:5]:
        cast_details[cast['imdb_id']] = {}
        cast_id = cast['imdb_id']
        cast_name = cast['name']
        for name in cast_name:
            cast_details[cast_id]['name'] = cast_name
            cast_details[cast_id]['frequent_co_actors'] = [{}]
            # co_cast_details = {}
        for co_cast in cast_details[cast_id]['frequent_co_actors']:
            co_cast['name'] = cast_name
            co_cast['imdb_id'] = cast_id
            co_cast['num_movies'] = 0
    print(cast_details)

for i in Top_movie_list[:2]:
    url = i['url']
    # print(url)
    # break
    pprint.pprint(analyse_co_actors(scrape_movie_details(url)))
    # print(url)

# pprint.pprint(movie[0]['url'])
# print(type(my_movies))
# print(analyse_co_actors(scrape_movie_details(Top_movie_list[7]['url'])))
# print(analyse_co_actors(dictionary(movie)))
# pprint.pprint(analyse_co_actors(dictionary(url)))

# def analyse_co_actors(movies_list):
#     movie = Top_movie_list
#     movie_url_list = []
#     for i in movies_list[:2]:
#         print(i['url'])
#         movie_url_list.append(i['url'])
#         cast_details = {}
#         for cast in movie_url_list['cast'][:5]:
#             cast_details[cast['imdb_id']] = {}
#             cast_id = cast['imdb_id']
#             cast_name = cast['name']
#             for name in cast_name:
#                 cast_details[cast_id]['name'] = cast_name
#                 cast_details[cast_id]['frequent_co_actors'] = [{}]
#                 # co_cast_details = {}
#             for co_cast in cast_details[cast_id]['frequent_co_actors']:
#                 co_cast['name'] = cast_name
#                 co_cast['imdb_id'] = cast_id
#                 co_cast['num_movies'] = 0
#         # print(cast_details)
#     print(movie_url_list)

# pprint.pprint(analyse_co_actors(scrape_movie_details(Top_movie_list)))
