import requests
import pprint
from bs4 import BeautifulSoup

def scrape_movie_details(movie_url):
    # url = "https://www.imdb.com/title/tt0066763/" 
    page = requests.get(movie_url)
    # print(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    # print(soup)

    director = []
    genre = []
    names = soup.find('div', class_='title_wrapper').h1.get_text()
    movie_time = soup.find('div', class_='title_wrapper').time.get_text().strip()
    Genre = soup.find('div', class_='subtext').a.get_text()
    genre.append(Genre)
    Director = soup.find('div', class_='credit_summary_item').a.get_text()
    director.append(Director)
    bio = soup.find('div', class_='summary_text').get_text().strip()
    poster = soup.find('div', class_='poster').img['src']
    similar = soup.find_all('div', class_='rec_item')
    similar_movie = []
    for i in similar:
        # print(i.a['href'])
        similar_movie.append(i.a['href'])

    table = soup.find_all('div', class_='txt-block')
    language = []
    for i in table:
        try:
            if i.find("h4").get_text()=="Language:": 
                language.append(i.find("a").get_text())
            if i.find("h4").get_text()=="Country:":
                Country = i.find("a").get_text()
                # print(i.find("a").get_text())
        except:
            pass

    # # print(language)
    # # print(Country)
    # # return language

    name = " "
    for i in names:
        if i == '(':
            break
        else:
            name=name+i
    movie_name = name.strip()
    # print(movie_name)

    run_time = []
    for i in movie_time:
        if i == 'h' or i == 'm' or i == 'i' or i == 'n' or i == " ":
            pass
        else:
            run_time.append(int(i))
    # print(run_time)

    time = run_time[0]*60
    i=1
    while i < len(run_time):
        time=time+run_time[i]
        i=i+1
    # print(time)

    dic={}
    dic['name'] = movie_name
    dic['director'] = director
    dic['Country'] = Country
    dic['Language'] = language
    dic['poster'] = poster
    dic['bio'] = bio
    dic['runtime'] = time
    dic['genre'] = genre
    dic['similar_movie'] = similar_movie

    # pprint.pprint(dic)
    return dic



pprint.pprint(scrape_movie_details("https://www.imdb.com/title/tt0066763/"))
