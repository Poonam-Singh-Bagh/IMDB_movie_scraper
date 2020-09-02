from task5movie_list_details import *

def analyse_movies_language(movies_list):
    language =  get_movie_list_details(scrape_top_list)
    lang_list = []
    for i in language:
        lang_list.extend(i['Language'])

    dict = {}
    for i in range(len(lang_list)):
        count = 0
        for j in range(len(lang_list)):
            if lang_list[i] ==  lang_list[j]:
                count=count+1
        dict[lang_list[i]] = count
    # pprint.pprint(dict)
    return dict

    # dict = {}
    # for i in language:
    #     count = 0
    #     for j in language:
    #         if i['Language'] == j['Language']:
    #             count=count+1
    #     print(i['Language'], ':', count)

    # #     dict[i['Language']] == count 
    # # pprint.pprint (dict)

# analyse_language = analyse_movies_language((get_movie_list_details(scrape_top_list)))
# pprint.pprint(analyse_language)
pprint.pprint(analyse_movies_language((get_movie_list_details(scrape_top_list))))



