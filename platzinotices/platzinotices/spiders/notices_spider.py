import scrapy
from common import config

# XPath categorías = //*[@id="menu_484494150"]/div/ul/li

class articlesSpider(scrapy.Spider):

    name = 'notices'
    CONFIG = config

    start_urls = CONFIG()['news_sites'][1]['categories']
    
    custom_settings = {
        'FEED_URI': 'cia.json',
        'FEED_FORMAT': 'json',
        'CONCURRENT_REQUEST': 24,
        'MEMUSAGE_LIMIT_MB': 2048,
        'ROBOTSTXT_OBEY': True,
        'FEED_EXPORT_ENCODING': 'utf-8',
        'DEPTH_LIMIT': 3
    }

    def parse_articles(self, response):
        pass

    def parse(self, response):
        select_article_link = response.xpath(CONFIG()['news_sites'][1]['article_links']).get()
        
        for i in range select_article_link:
            yield response.follow(select_article_link[i], callback = pass)