from task13scrape_movie_details import *
from task1top_movies import *

def analyse_actors(movies_list):
    details = []
    for movie in Top_movie_list[:50]:
        movie_url = movie['url']
        cast_details = scrape_movie_details(movie_url)
        details.append(cast_details)
    # return details
    actor_details = {}
    for i in details:
        for cast in i['cast']:
            print(cast)
            # count = 0
            cast_id = cast['imdb_id']
            cast_name = cast['name']
            # print(cast_name) 
            # if cast_name not in actor_details: 
            #     actor_details[cast_id] = {"name":cast_name, "num":1} 
            # else:
            #     min = actor_details[cast_id] 
            #     min['num'] +=1 
            
    return actor_details
pprint.pprint(analyse_actors(Top_movie_list))


    # print(actor)
    # for i in details:
    #     for cast in i['cast']:
    #         # count = 0
    #         cast_id = cast['imdb_id']
    #         cast_name = cast['name']
    #         # print(cast_name)
    #         if cast_name not in actor_details:
    #             actor_details[cast_id] = {}
    #             actor = actor_details[cast_id]
    #             # for actor in actor_details[cast_id]:
    #             actor['name'] = cast_name
    #             actor['num_movies'] +=1
            
    # return actor_details
           
# pprint.pprint(Top_movie_list)
# pprint.pprint(analyse_actors(Top_movie_list))


# def analyse_actors(movies_list):
#     details = []
#     for movie in Top_movie_list[:3]:
#         movie_url = movie['url']
#         cast_details = scrape_movie_details(movie_url)
#         details.append(cast_details)
#     # return details
#     actor_details = {}
#     for i in details:
#         key = i['cast']
#         # print(i)
#         # acotr_list = []
#         # for cast in i['cast']:
#         #     # count = 0
#         #     cast_id = cast['imdb_id']
#         #     cast_name = cast['name']
#         #     print(cast_name)
#         #     if cast_name not in actor_details:
#         #         actor_details[cast_id] = {}
#         #         actor = actor_details[cast_id]
#         #         actor['name'] = cast_name
#         #         actor['num_movies'] = 0
#                 # for actor 
#     # return actor_details

# pprint.pprint(analyse_actors(Top_movie_list))


# def analyse_actors(movies_list):
#     # movies_list = Top_movie_list
#     list = []
#     for movie in Top_movie_list[:10]:
#         movie_url = movie['url']
#         cast_details = scrape_movie_details(movie_url)
#         list.append(cast_details)
#     details = {}
#     for i in list:
#         for cast in i['cast']:
          
#             cast_id = cast["imdb_id"]
#             cast_name = cast["name"]
            
#             if cast_id in details:
#                 actor["num_movie"] += 1
#             else:
#                 details[cast_id] = {}
#                 actor = details[cast_id]
#                 actor["name"]= cast_name
#                 actor["num_movie"] = 1
#     return details
# pprint.pprint(analyse_actors(Top_movie_list))