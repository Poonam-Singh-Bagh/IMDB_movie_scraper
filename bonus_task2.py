# import requests
# import pprint
# from bs4 import BeautifulSoup

# def rating(url):
#     page = requests.get(url)
#     soup = BeautifulSoup(page.text, 'html.parser')
#     # print(soup)
#     table = soup.find('table')
#     # print(table)
#     trs = table.find_all('tr')
#     for i in trs:
#         tr = i.get_text()
#         td = tr.find('td', class_='leftAligned')
#         print(td)
#     # trs = tbody.find('td')
#     # print(trs)

# pprint.pprint(rating("https://www.imdb.com/title/tt0066763/ratings?ref_=tt_ov_rt"))

# a = (23+True)/(False*34)
# print(a)

# print(True == 2)
