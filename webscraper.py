# Helper functions

# Returns array of js object containing data from id='oferta'
def get_data_from_id_oferta(soup):
    soup = soup
    # get part of HTML
    id_oferta = soup.find(id='oferta')
    #get all elements having givn class
    class_pbc = id_oferta.find_all('div', class_='pricing-block-content') # Returns ResultSet (list)
    # add data as js object
    data = []
    for element in class_pbc:
        heading = element.h3.text
        detail = element.p.text
        link = element.a['href']
        img = element.img['src']
        item = {'heading': heading, 'detail': detail, 'link': link, 'img': img}
        data.append(item)

    return data

def extractDetails(soup):
    soup = soup
    course_name = soup.find('h2').text
    categories = soup.find('h3').text

    id_about = soup.find(id='about')    
    img = id_about.img['src']

    # get main content as BeautilSoup
    content = soup.find('div', class_='alignToPhoto')

    # get texts from content

    # short_desc = content.find('p').text
    # # remove first child
    # content.p.extract()

    # common_desc = content.find('p').text
    # content.p.extract()

    # special_offer = content.find('p').text
    # content.p.extract()
    # special_offer += content.find('p').text
    # content.p.extract()

    long_desc = ''
    for string in content.stripped_strings:
        long_desc += '<p>' + string + '</p>\n'

    data = {'course_name': course_name,
                'categories': categories,
                'img': img,
                'long_desc': long_desc
                }
    return data

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
data_home = get_data_from_id_oferta(soup)
print(data_home)

# 2. Get data from subpages
data_subpage = []

for d in data_home:
    subpage = d['link']
    page = req.get('http://www.konwersatoriummuzyczne.pl/' + subpage)
    soup = BeautifulSoup(page.content, 'html.parser')

    data = get_data_from_id_oferta(soup)
    data_subpage.append(data)
 
    # add long_desc to data_main
    long_desc = soup.find(id='about').text
    d['long_desc'] = long_desc

# 3. Get detail data
# for d in data_subpage:

data_details = []

for row in data_subpage:
    for col in row:
        subpage = col['link']
        page = req.get('http://www.konwersatoriummuzyczne.pl/' + subpage)
        soup = BeautifulSoup(page.content, 'html.parser')

        data = extractDetails(soup)
        data_details.append(data)

print(data_details)
print('By')