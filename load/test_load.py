import unittest
import pandas as pd
import logging
import re
import datetime
logging.basicConfig(level=logging.INFO)
from load import clean_body, clean_tags, clean_images_list, cleaning_vanguardia_images, clean_empty_spaces, string_to_datetime

today = datetime.datetime.now()
logger = logging.getLogger(__name__)
test_list = []

class Test_Load(unittest.TestCase):
    logger.info('Starting test to the database.')
    def test_clean_body(self):
        ''' Test that verifies the integrity of the body of the articles '''
        df = pd.read_csv('clean_articles_test.csv')
        df = clean_body(df)
        for body in df['body']:
            self.assertIsNotNone(body)

    def test_clean_tags(self):
        ''' Test that verifies that the tags are not note and that it returns a list '''
        df = pd.read_csv('clean_articles_test.csv')
        df = clean_tags(df)
        for tag in df['tags']:
            self.assertIsNotNone(tag)
            self.assertEqual(type(tag), type(test_list))

    def test_clean_images_list(self):
        ''' Test that transform the content of the df['images'] from string to a list '''
        df = pd.read_csv('clean_articles_test.csv')
        df = clean_images_list(df)
        for image in df['images']:
            self.assertEqual(type(image), type(test_list))

    def test_clean_empty_spaces(self):
        ''' Test that verifies that the content for the series subtitle, category_long and author is not none '''
        df = pd.read_csv('clean_articles_test.csv')
        df = clean_empty_spaces(df)
        for data in range(len(df)):
            self.assertIsNotNone(df['subtitle'][data])
            self.assertIsNotNone(df['category_long'][data])
            self.assertIsNotNone(df['author'][data])

    def test_string_to_datetime(self):
        ''' Test that verifies that the publication_date series is a datetime type '''
        df = pd.read_csv('clean_articles_test.csv')
        df = string_to_datetime(df)
        for date in df['publication_date']:
            self.assertEqual(type(date), type(today))


if __name__ == "__main__":
    unittest.main()