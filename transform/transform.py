import os.path
import pandas as pd
import logging
import csv
import datetime
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

def _delete_empty_titles_and_bodies(df):
    df = df.dropna()
    for title in range(len(df)):
        if df.loc[title, 'title'] == '' or df.loc[title, 'body'] == '[]':
            df.drop(title, axis = 0, inplace = True)

    return df

def _clean_df_string(df):
    for item in range(len(df)):
        df['title'][item] = df['title'][item][2:-2]
        df['subtitle'][item] = df['subtitle'][item][2:-2]
        df['author'][item] = df['author'][item][2:-2]
        df['category_long'][item] = df['category_long'][item][2:-2]
        df['body'][item] = df['body'][item][2:-2]
        df['tags'][item] = df['tags'][item][2:-2]
        df['images'][item] = df['images'][item][2:-2]

    return df

def _clean_datetime(df):
    for dt in range(len(df)):
        df['publication_date'][dt] = df['publication_date'][dt].replace('\'','')
        df['publication_date'][dt] = df['publication_date'][dt].replace('[','')
        df['publication_date'][dt] = df['publication_date'][dt].replace(']','')
    df['publication_date'] = pd.to_datetime(df['publication_date'])
    return df

def _delete_first_space_categories(df_categories):
    df_categories = df_categories.dropna()
    df_categories = df_categories.reset_index()
    df_categories.drop(['index'], axis = 1, inplace = True)

    for category in range(len(df_categories)):
        df_categories.loc[category] = df_categories.loc[category, 'categories'][0].replace(" ", "")+df_categories.loc[category, 'categories'][1:]
        df_categories.loc[category] = df_categories.loc[category, 'categories'].capitalize()
    return df_categories

def main(df, df_categories):
    df = pd.read_csv(df)
    logger.info('Starting cleaning process for articles.')
    df = _delete_empty_titles_and_bodies(df)
    df = _clean_datetime(df)
    df = _clean_df_string(df)
    print(df)
    df.to_csv('clean_articles.csv', index = False)
    logger.info('Cleaning process for articles completed.')
    df_cat = pd.read_csv(df_categories)
    logger.info('Starting cleaning process for categories.')
    df_cat = _delete_first_space_categories(df_cat)
    df_cat.to_csv('clean_categories.csv', index = False)
    logger.info('Cleaning process for categories completed.')

if __name__ == "__main__":
    main('articles.csv', 'categories.csv')
    