import pymongo
import logging
import pandas as pd
import re
import numpy as np
from client import client
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

db = client['news_db']
logger.info(f'Conecting to DB {db.name}.')
data_articles = []
data_categories = []


def _clean_body(df):
    df['body'] = df['body'].str.replace("',", "---")
    df['body'] = df['body'].str.replace("'", '')
    df['body'] = df['body'].str.replace("[", '')
    df['body'] = df['body'].str.replace("]", '')
    df['body'] = df['body'].str.split("---")
    #for body in range(len(df)):
        
        
        
    return df

def _clean_tags(df):
    df['tags'] = df['tags'].fillna(method = 'bfill')
    df['tags'] = df['tags'].str.replace('\',', '---')
    df['tags'] = df['tags'].str.replace('[', '')
    df['tags'] = df['tags'].str.replace('\'', '')
    df['tags'] = df['tags'].str.replace(']', '')
    df['tags'] = df['tags'].str.split("---")
            
    return df


def _clean_images_list(df):
    df['images'] = df['images'].fillna('')
    
    for img in range(len(df['images'])):
        df['images'][img] = df['images'][img].split(',')
        for item in range(len(df['images'][img])):
            df['images'][img][item] = df['images'][img][item].replace('\'', "")
            
    return df


def _cleaning_vanguardia_images(df_articles):
    for df in range(len(df_articles)):
        if df_articles['host'][df] == 'https://www.vanguardia.com':
            for url in range(len(df_articles['images'][df])):
                df_articles['images'][df][url] = "".join(re.findall(r'[\w]{3}\.[\w\-\.\/]+\.[\w]{3}', df_articles['images'][df][url]))
    return df_articles


def _clean_empty_spaces(df):
    df['subtitle'] = df['subtitle'].fillna('')
    df['category_long'] = df['category_long'].fillna(method = 'bfill')
    df['author'].fillna(df['host'], inplace = True)
    
    return df

def _string_to_datetime(df):
    df['publication_date'] = pd.to_datetime(df['publication_date'])
    return df

df_articles = pd.read_csv('clean_articles.csv')
df_articles = _clean_tags(df_articles)
df_articles = _clean_body(df_articles)
df_articles = _clean_images_list(df_articles)
df_articles = _cleaning_vanguardia_images(df_articles)
df_articles = _clean_empty_spaces(df_articles)
df_articles = _string_to_datetime(df_articles)
df_categories = pd.read_csv('clean_categories.csv')

logger.info(f'Accessing to collections.')
collection_articles = db['news']
collection_categories = db['categories']

logger.info(f'Parsing article data.')
for article in range(len(df_articles)):
    data_articles.append({
        'title': df_articles['title'][article],
        'subtitle': df_articles['subtitle'][article],
        'images': df_articles['images'][article],
        'body': df_articles['body'][article],
        'tags': df_articles['tags'][article],
        'author': df_articles['author'][article],
        'host': df_articles['host'][article],
        'news_url': df_articles['news_url'][article],
        'publication_date': df_articles['publication_date'][article],
        'category': df_articles['category_long'][article]
    })
logger.info(f'Parsing Category data.')
for category in range(len(df_categories)):
    data_categories.append({'categories':df_categories['categories'][category]})


logger.info(f'Saving data into database.')
if data_articles:
    collection_articles.insert_many(data_articles)
    logger.info(f'{len(data_articles)} articles inserted into database.')
if data_categories:
    collection_categories.insert_many(data_categories)
    logger.info(f'{len(data_categories)} categories inserted into database.')

logger.info(f'Closing database {db.name}.')

client.close()