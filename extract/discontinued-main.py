import logging
import requests
import re
from bs4 import BeautifulSoup
from common import config
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)
is_well_formed_link = re.compile(r'^https?://.+/.+$')
is_root_path = re.compile(r'^/.+$')
config = config

def _build_link(host, link):
    ''' Function that builds properly a url '''
    if is_well_formed_link.match(link):
        return link
    elif is_root_path.match(link):
        return f'{host}{link}'
    else:
        return f'{host}/{link}'

def _category_links_extraction(host, iterator):
    ''' Function that returns a list of the category links '''
    logger.info(f'Extracting category list for {host}')
    # Variables definition
    categories_selector = config()['news_sites'][iterator]['categories']
    categories_selector_attributes = config()['news_sites'][iterator]['categories_attributes']
    find_selector = config()['news_sites'][iterator]['find_categories']
    find_selector_attributes = config()['news_sites'][iterator]['find_categories_attributes']

    # Requesting info from the newspaper
    news_sites_request = requests.get(host)
    news_sites_soup = BeautifulSoup(news_sites_request.text, 'lxml')

    # Selecting the category list of the newspaper
    categories_list = news_sites_soup.find(categories_selector, attrs = categories_selector_attributes).find_all(find_selector, attrs = find_selector_attributes)

    # Extracting the links for each category
    categories_links = []
    for category in categories_list:
        categories_links.append(host+category.a.get('href'))

    return categories_links


def _articles_links_extraction(url_list, iterator):
    ''' Function that extracts the urls for each category, and returns it in a list. '''
    # Variables definition
    host = config()['news_sites'][iterator]['url']
    article_container_selector = config()['news_sites'][iterator]['articles']
    article_container_selector_attributes = config()['news_sites'][iterator]['articles_attributes']
    article_selector = config()['news_sites'][iterator]['find_articles']
    article_selector_attributes = config()['news_sites'][iterator]['find_articles_attributes']
    article_list = []

    for link in url_list:
        # Requesting info for each category url.
        logger.info(f'Starting links extraction for {link}')
        try:
            category_request = requests.get(link)
            category_soup = BeautifulSoup(category_request.text, 'lxml')
            # type(category_soup)
        except Exception as e:
            logger.info(f'Error with server {link}')
        
        try:
            # Selecting the article box.
            articles_container = category_soup.find(article_container_selector, attrs = article_container_selector_attributes).find_all(article_selector, attrs = article_selector_attributes)

            # Building the url for each article
            for article in articles_container:
                article_list.append(_build_link(host, article.a.get('href')))
        except Exception as e:
            logger.info(f'There is no article.')

    # Deleting repeated articles
    article_list = list(set(article_list))

    return article_list


def _news_extraction(url_list, iterator):
    # Variables definition
    return_dict = dict
    # Queries
    news_container = config()['news_sites'][iterator]['queries']['news_container']
    news_container_attributes = config()['news_sites'][iterator]['queries']['news_container_attributes']
    title = config()['news_sites'][iterator]['queries']['title']
    title_attributes = config()['news_sites'][iterator]['queries']['title_attributes']
    subtitle = config()['news_sites'][iterator]['queries']['subtitle']
    subtitle_attributes = config()['news_sites'][iterator]['queries']['subtitle_attributes']
    content = config()['news_sites'][iterator]['queries']['content']
    content_attributes = config()['news_sites'][iterator]['queries']['content_attributes']
    images = config()['news_sites'][iterator]['queries']['images']
    images_attributes = config()['news_sites'][iterator]['queries']['images_attributes']
    #   category_long: ''
    #   category_long_attributes: {}
    tags = config()['news_sites'][iterator]['queries']['tags']
    tags_attributes = config()['news_sites'][iterator]['queries']['tags_attributes']
    author = config()['news_sites'][iterator]['queries']['author']
    author_attributes = config()['news_sites'][iterator]['queries']['author_attributes']
    publication_date = config()['news_sites'][iterator]['queries']['publication_date']
    publication_date_attributes = config()['news_sites'][iterator]['queries']['publication_date_attributes']
    categories = config()['news_sites'][iterator]['queries']['categories']
    categories_attributes = config()['news_sites'][iterator]['queries']['categories_attributes']
    

if __name__ == '__main__':
    for i in range(len(config())):
        host = config()['news_sites'][i]['url']
        logger.info(f'Begining scraper for {host}')
        categories = _category_links_extraction(host, i)
        articles_links = _articles_links_extraction(categories, i)
        print(articles_links)
        print(len(articles_links))