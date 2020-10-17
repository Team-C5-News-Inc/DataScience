import logging
import requests
from bs4 import BeautifulSoup
from common import config
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

config = config

def category_links_extraction(host, iterator):
    ''' Returns a list of the category links '''
    logger.info(f'Extracting category list for {host}')
    # Variables definition
    categories_selector = config()['news_sites'][iterator]['categories']
    categories_selector_attributes = config()['news_sites'][iterator]['categories_attributes']
    find_selector = config()['news_sites'][iterator]['find']
    find_selector_attributes = config()['news_sites'][iterator]['find_attributes']

    # Requesting info from the newspaper
    news_sites_request = requests.get(host)
    news_sites_soup = BeautifulSoup(news_sites_request.text, 'lxml')

    # Selecting the category list of the newspaper
    categories_list = news_sites_soup.find(categories_selector, attrs = categories_selector_attributes).find_all(find_selector, attrs = find_selector_attributes)

    # Extracting the links of each category
    categories_links = []
    for category in categories_list:
        categories_links.append(host+category.a.get('href'))

    return categories_links

url = config()['news_sites'][0]['url']

links = category_links_extraction(url, 0)
print(links)
for link in links:
    logger.info(f'Starting links extraction for {link}')
    try:
        category_request = requests.get(link)
        category_soup = BeautifulSoup(category_request, 'lxml')
        # type(category_soup)
    except Exception as e:
        logger.info(f'Error with server {link}')
        break
    try:
        links_container = category_soup.find('section', attrs = {'id':'r01-c01'}).find_all('article')
        # type(links_container)
 
# if __name__ == '__main__':
#     for i in range(len(config())):
#         host = config()['news_sites'][i]['url']
#         logger.info(f'Begining scraper for {host}')
#         print(category_links_extraction(host, i))