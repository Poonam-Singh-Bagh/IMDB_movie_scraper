import time
import random

# for count in range(5):
#     print(time.ctime())
#     # Prints the current time with a five second difference
#     time.sleep(random.randint(1,3))

from task4scrape_movie_details import *
from task1top_movies import *

def get_movie_list_details(movies_list ):

    Top_movie_list = scrape_top_list()
    movieDetails = []
    for i in Top_movie_list[0:10]:
        print(time.ctime())
        time.sleep(random.randint(1,3))
        seconds = time.time()
        # p = time
        print(seconds)
        URL = scrape_movie_details(i['url']) 
        print(URL)
    #     movieDetails.append(URL)
    # return movieDetails
    
pprint.pprint(get_movie_list_details(scrape_top_list))
# movie_details = (get_movie_list_details(scrape_top_list))
# get_movie_list_details(scrape_top_list)
