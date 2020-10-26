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
        if df.loc[title, 'title'] == '[]' or df.loc[title, 'body'] == '[]':
            df.drop(title, axis = 0, inplace = True)

    return df


def _delete_first_space_categories(df_categories):
    df_categories = df_categories.dropna()
    df_categories = df_categories.reset_index()
    df_categories.drop(['index'], axis = 1, inplace = True)

    for category in range(len(df_categories)):
        for category in range(len(df_categories)):
            df_categories.loc[category] = df_categories.loc[category, 'categories'][0].replace(" ", "")+df_categories.loc[category, 'categories'][1:]
            df_categories.loc[category] = df_categories.loc[category, 'categories'].capitalize()
    return df_categories

def main(df, df_categories):
    df = pd.read_csv(df)
    logger.info('Starting cleaning process for articles.')
    df = _delete_empty_titles_and_bodies(df)
    df.to_csv('clean_articles.csv', index = False)
    logger.info('Cleaning process for articles completed.')
    df_cat = pd.read_csv(df_categories)
    logger.info('Starting cleaning process for categories.')
    df_cat = _delete_first_space_categories(df_cat)
    df_cat.to_csv('clean_categories.csv', index = False)
    logger.info('Cleaning process for categories completed.')

if __name__ == "__main__":
    main('articles.csv', 'categories.csv')
    