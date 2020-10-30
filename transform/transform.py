import datetime
import os.path
import pandas as pd
import logging
import csv
import datetime
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)
today = datetime.datetime.now().strftime('%Y-%m-%d')

def _delete_empty_titles_and_bodies(df):
    df[['title']] = df[['title']].dropna()
    df[['body']] = df[['body']].dropna()
    
    return df

def _clean_df_string(df):
    df['title'] = df['title'].str[2:-2]
    df['subtitle'] = df['subtitle'].str[2:-2]
    df['author'] = df['author'].str[2:-2]
    df['category_long'] = df['category_long'].str[2:-2]
    df['body'] = df['body'].str[2:-2]
    df['tags'] = df['tags'].str[2:-2]
    df['images'] = df['images'].str[2:-2]

    return df

def _clean_datetime(df):
    df['publication_date'] = df['publication_date'].str.replace('\'','')
    df['publication_date'] = df['publication_date'].str.replace('[','')
    df['publication_date'] = df['publication_date'].str.replace(']','')
    for date in range(len(df['publication_date'])):
        if len(df['publication_date'][date]) == 0:
            df['publication_date'][date] = today

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

def main(df_articles, df_categories):
    df = pd.read_csv(df_articles)
    logger.info('Starting cleaning process for articles.')
    df = _clean_df_string(df)
    df = _delete_empty_titles_and_bodies(df)
    df = _clean_datetime(df)
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
    