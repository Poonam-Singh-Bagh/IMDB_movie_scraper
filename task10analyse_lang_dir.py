from task5movie_list_details import *

def analyse_language_and_directors(movies_list):
    movies = get_movie_list_details(scrape_top_list)
    dict = {}
    for movie in movies:
        for dir in movie['director']:
            dict[dir] = {}
    # pprint.pprint(dict)
    for movie in movies:
        for dir in movie['director']:
            if dir in dict:
                for lang in movie['Language']:
                    dict[dir][lang]=0
    # pprint.pprint(dict)
    for movie in movies:
        for dir in movie['director']:
            for lang in movie['Language']:
                if dir in dict:
                    dict[dir][lang]+=1
    # pprint.pprint(dict)
    return dict

pprint.pprint(analyse_language_and_directors(movie_details))


    # for i in dict:
    #     dic ={}
    #     count = 0
    #     for j in movies:
    #         # print(j['director'])
    #         if i in j['director']:
    #             for k in j['Language']:
    #                 count=count+1
    #                 # print(k)
    # #             print()
    # #             print(j['Language'])
    #         dic[k] = count
    #     pprint.pprint(dic)
    #     dict = dic
    # # pp[dict] = dic
    # pprint.pprint(dict)
    # # #         # print(j)'''

    # dict = {}
    # for i in range(len(director_list)):
    #     # print(director_list[i])
    #     # print("======================================================")
    #     dic = {}
    #     list = []
    #     for k in range(len(movies)):
    #         # print(movies[k]['director'])
    #         # print("***********************************************")
    #         # list = []
    #         for n in range(len(movies[k]['director'])):
    #             if director_list[i] == movies[k]['director'][n]:
    #                 p = {}
    #                 for m in range(len(movies[k]['Language'])):
    #                     print(movies[k]['Language'][m])
    #                     list.append(movies[k]['Language'][m])
    #             print(movies[k]['director'][n])
    #             print("/////////////////////////////////////////////////")
    # print(list)
    #         # list = []
            # if director_list[i] == movies[k]['director']:
            #     print(movies[k]['Language'])
            #     list.append(movies[k]['Language'])
        # print(list)   
            
            # print(movies[k]['director'])
            # print("***********************************************")
            # for j in movies[k]:
            #     print(j)
            #     print("/////////////////////////////////////////////////")
            #     if dict[i] == movies[j]['director']
            # dic = {}
            # dir = 0
            # for j in range(len(director_list)):
            #     if director_list[i] ==  director_list[j]:
            #         dir=dir+1
            # print(dir)
                # if director_list[i] == movies[j]['director']:
                #     print("punnu")
                #     # punnu = {}
                #     for i in range(len(lang_list)):
                #         lang = 0
                #         for j in range(len(lang_list)):
                #             if lang_list[i] ==  lang_list[j]:
                #                 lang=lang+1
                #         punnu[lang_list[i]] = lang
                #     return (punnu)
        # dict[director_list[i]] = count
    #     dict[director_list[i]] = dic
    # pprint.pprint(dict) 


    # for j in dict:
    #     for j in movies:
            

    #         # if j in movies[i]['director']:
    #         pprint.pprint(j)
    #         #     for i in range(len(lang_list)):
    #         #         lang = 0
    #         #         for j in range(len(lang_list)):
    #         #             if lang_list[i] ==  lang_list[j]:
    #         #                 lang=lang+1
    #         #         punnu[lang_list[i]] = lang
    #         #     return (punnu)
    #         # print(j)
    #     # if director_list[i] in movies[i]:
    #     #     print("punnu")
    #     #     # punnu = {}
    #     #     for i in range(len(lang_list)):
    #     #         lang = 0
    #     #         for j in range(len(lang_list)):
    #     #             if lang_list[i] ==  lang_list[j]:
    #     #                 lang=lang+1
    #     #         punnu[lang_list[i]] = lang
    #     #     return (punnu)

# pprint.pprint(analyse_language_and_directors(movie_details))



'''def analyse_language_and_directors(movies_list):
    movies = get_movie_list_details(scrape_top_list)
    # lang_list = []
    # director_list = []
    dict = {}
    for i in movies:
        for j in i['Language']:
            print("punnu")
            if j not in dict:
                dict[j] = 0
    print(dict)
        #     print("punnu")
    #         dict[i['Language']]=0
    #         print(i['Language'])
    # #     dict[i['Language']]=0
    # pprint.pprint(dict)
pprint.pprint(analyse_language_and_directors((get_movie_list_details(scrape_top_list))))'''
