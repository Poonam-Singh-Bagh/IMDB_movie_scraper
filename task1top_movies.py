import requests
import json
import pprint
from bs4 import BeautifulSoup


url = "https://www.imdb.com/india/top-rated-indian-movies/"
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

def scrape_top_list():
    main_div = soup.find('div',class_='lister')
    tbody = main_div.find('tbody',class_='lister-list')
    trs = tbody.find_all('tr')

    movie_rank = []
    movie_released = []
    movie_list = []
    movie_url = []
    movie_rating = []
    for tr in trs:
        position = tr.find('td', class_='titleColumn').get_text().strip()
        # print(position)
        rank = " "
        for i in position:
            if "." in i:
                break
            else:
                rank=rank+i
        movie_rank.append(rank)
        title = tr.find('td', class_='titleColumn').a.get_text()
        movie_list.append(title)
        year = tr.find('td',class_='titleColumn').span.get_text()
        movie_released.append(year)
        url = tr.find('td', class_='titleColumn').a['href']
        link = "https://www.imdb.com"+url
        movie_url.append(link)
        rating = tr.find('td', class_='ratingColumn imdbRating').get_text().strip()
        movie_rating.append(rating)

    # return movie_url


    movie_released_year = []
    for i in movie_released:
        var = list(i)
        value = var[1]+var[2]+var[3]+var[4]
        number = int(value)
        movie_released_year.append(number)
    # print(movie_released_year)

    # Top_movies = []
    # for index in range(0,10):
    #     dic = {}
    #     dic['name'] = movie_list[index]
    #     dic['year'] = movie_released_year[index]
    #     dic['position'] = movie_rank[index]
    #     dic['rating'] = movie_rating[index]
    #     dic['url'] = movie_url[index]
    #     Top_movies.append(dic)
    #     # index=index+1
    # return Top_movies


    Top_movies = []
    for index in range(len(movie_list)):
        dic = {}
        dic['name'] = movie_list[index]
        dic['year'] = movie_released_year[index]
        dic['position'] = movie_rank[index]
        dic['rating'] = movie_rating[index]
        dic['url'] = movie_url[index]
        Top_movies.append(dic)
    return Top_movies
    # pprint.pprint(Top_movies)

Top_movie_list = scrape_top_list()
# movie = Top_movie_list[3:7]['url']
# pprint.pprint(movie)
# pprint.pprint(scrape_top_list())
# pprint.pprint(Top_movie_list)
# scrape_top_list()



