from task4scrape_movie_details import *
from task1top_movies import *
import pathlib
import json


'''def caching(url):
    # Top_movie_list = scrape_top_list()
    # movieDetails = []
    # for i in Top_movie_list[0:10]:
    #     dict = scrape_movie_details(i['url']) 
    #     movieDetails.append(dict)
    #     URL = i['url']
    URL = url.split("/")
    fileId = URL[4]
    # print(fileId)
    fileName = ("caching/"+fileId+".json")
    # print(fileName)
    filePath = pathlib.Path(fileName)

    if filePath.exists():
        # print("true")
        with open(fileName,'r') as file:
            # print(fileName)
            data = json.load(file)
            pprint.pprint(data)
    else:
        # print("false")
        # url = "https://www.imdb.com/title/tt0066763/" 
        page = requests.get(url)
        # print(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        # print(soup)

        director = []
        genre = []
        names = soup.find('div', class_='title_wrapper').h1.get_text()
        # print(names)
        movie_time = soup.find('div', class_='title_wrapper').time.get_text().strip()
        # print(movie_time)
        Genre = soup.find('div', class_='subtext').a.get_text()
        genre.append(Genre)
        # print(genre)
        Director = soup.find('div', class_='credit_summary_item').a.get_text()
        director.append(Director)
        # print(director)
        bio = soup.find('div', class_='summary_text').get_text().strip()
        # print(bio)
        poster = soup.find('div', class_='poster').img['src']
        # print(poster)
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
       
        with open(fileName,'w+') as file:
            # print(fileName)
            # print("name")
            file.write(json.dumps(dic))
        # pprint.pprint(dic)    
        return dic

caching("https://www.imdb.com/title/tt0066763/")'''


def caching(url):
    # Top_movie_list = scrape_top_list()
    # movieDetails = []
    # for i in Top_movie_list[0:10]:
    #     dict = scrape_movie_details(i['url']) 
    #     movieDetails.append(dict)
    #     URL = i['url']
    URL = url.split("/")
    fileId = URL[4]
    # print(fileId)
    fileName = ("caching/"+fileId+".json")
    # print(fileName)
    filePath = pathlib.Path(fileName)

    if filePath.exists():
        # print("true")
        with open(fileName,'r') as file:
            # print(fileName)
            data = json.load(file)
            pprint.pprint(data)
    else:
        details = scrape_movie_details(url)
        with open(fileName,'w+') as file:
            # print(fileName)
            # print("name")
            file.write(json.dumps(dic))
        # pprint.pprint(dic)    
        return dic

caching("https://www.imdb.com/title/tt0066763/")


