import logging
import requests
from bs4 import BeautifulSoup
from common import config
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

config = config

def category_links_extraction(host, iterator):
    ''' Function that returns a list of the category links '''
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


def articles_links_extraction(url_list, iterator):
    ''' Function that extracts the urls for each category, and returns it in a list. '''
    article_container_selector = config()['news_sites'][iterator]['articles']
    article_container_selector_attributes = config()['news_sites'][iterator]['articles_attributes']
    article_selector = config()['news_sites'][iterator]['find_articles']
    article_selector_attributes = config()['news_sites'][iterator]['find_articles_attributes']
    article_list_tmp = []
    article_list = []
    for link in url_list:
        logger.info(f'Starting links extraction for {link}')
        try:
            category_request = requests.get(link)
            category_soup = BeautifulSoup(category_request.text, 'lxml')
            # type(category_soup)
        except Exception as e:
            logger.info(f'Error with server {link}')
            
        try:
            articles_container = category_soup.find(article_container_selector, attrs = article_container_selector_attributes).find_all(article_selector, attrs = article_selector_attributes)
            for article in articles_container:
                article_list_tmp.append(host + article.a.get('href'))
        except Exception as e:
            logger.info(f'There is no article.')

    # Deleting repeated articles 
    for i in article_list_tmp:
        if i not in article_list:
            article_list.append(i)

    return article_list


if __name__ == '__main__':
    for i in range(len(config())):
        host = config()['news_sites'][i]['url']
        logger.info(f'Begining scraper for {host}')
        categories = category_links_extraction(host, i)
        articles_links = articles_links_extraction(categories, i)
        print(articles_links)
        print(len(articles_links))