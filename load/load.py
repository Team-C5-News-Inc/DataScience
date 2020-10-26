import pymongo
import logging
import pandas as pd
from client import client
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

db = client['news_inc']
logger.info(f'Conecting to DB {db.name}.')
data_articles = []
data_categories = []

df_articles = pd.read_csv('clean_articles.csv')
df_categories = pd.read_csv('clean_categories.csv')

logger.info(f'Accessing to collections.')
collection_articles = db['articles']
collection_categories = db['categories']

logger.info(f'Parsing article data.')
for article in range(len(df_articles)):
    data_articles.append({
        'title': df_articles['title'][article],
        'subtitle': df_articles['subtitle'][article],
        'body': df_articles['body'][article],
        'category_long': df_articles['category_long'][article],
        'tags': df_articles['tags'][article],
        'author': df_articles['author'][article],
        'publication_date': df_articles['publication_date'][article],
        'news_url': df_articles['news_url'][article],
        'host': df_articles['host'][article]
    })
logger.info(f'Parsing Category data.')
for category in range(len(df_categories)):
    data_categories.append({'categories':df_categories['categories'][category]})

logger.info(f'Saving data into database.')
collection_articles.insert_many(data_articles)
collection_categories.insert_many(data_categories)

logger.info(f'Closing database {db.name}.')
client.close()