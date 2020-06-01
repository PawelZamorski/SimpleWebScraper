# https://requests.readthedocs.io/en/master/#
import requests as req
# https://pypi.org/project/beautifulsoup4/
from bs4 import BeautifulSoup

# get page
page = req.get('http://www.konwersatoriummuzyczne.pl')
# parse
soup = BeautifulSoup(page.content, 'html.parser')
# indent HTML
# pretty_soup = soup.prettify()
# print
# print(pretty_soup)

# 1. Get data from home page
# get part of HTML
id_oferta = soup.find(id='oferta')
#get all elements having givn class
class_pbc = id_oferta.find_all('div', class_='pricing-block-content') # Returns ResultSet (list)
# add data as js object
data_home = []
for element in class_pbc:
    heading = element.h3.text
    detail = element.p.text
    link = element.a['href']
    img = element.img['src']
    item = {'heading': heading, 'detail': detail, 'link': link, 'img': img}
    data_home.append(item)

