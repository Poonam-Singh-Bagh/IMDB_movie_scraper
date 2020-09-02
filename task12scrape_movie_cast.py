import requests
import pprint
from bs4 import BeautifulSoup
import pathlib
import json

def scrape_movie_cast(movie_caste_url):

    url = movie_caste_url.split('/')
    fileId = url[4]
    # print(url[4])
    fileName = ("film_cast/"+fileId+".json")
    # print(fileName)
    filePath = pathlib.Path(fileName)

    if filePath.exists():
        # print("True")
        with open(fileName,'r') as file:
            # print("punnu")
            data = json.load(file)
            return data
    else:
        # print("False")
        page = requests.get(movie_caste_url)
        soup = BeautifulSoup(page.text, 'html.parser')
        table = soup.find('table', class_='cast_list')
        casts = table.find_all('td', class_='')

        cast_list = []
        for cast in casts:
            actors = {}
            imdb_id = cast.a['href'][6:15]
            # print(imdb_id)
            name = cast.get_text().strip()
            # print(name)
            actors['imdb_id'] = imdb_id
            actors['name'] = name
            cast_list.append(actors)
        with open(fileName,'w+') as file:
            print("punnu")
            file.write(json.dumps(cast_list))
        return cast_list
    
# scrape_movie_cast("https://www.imdb.com/title/tt0066763/fullcredits?ref_=tt_cl_sm#cast")
# pprint.pprint(scrape_movie_cast("https://www.imdb.com/title/tt0066763/fullcredits?ref_=tt_cl_sm#cast"))