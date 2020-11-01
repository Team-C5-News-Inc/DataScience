import pandas as pd
import pandas.testing as pd_test
import unittest
import logging
import datetime
logging.basicConfig(level = logging.INFO)
from transform import delete_empty_titles_and_bodies, clean_df_string, clean_datetime, delete_first_space_categories

today = datetime.datetime.now()
logger = logging.getLogger(__name__)

class Test_Transform(unittest.TestCase):
    logger.info('Starting test for the data transformation.')
    def test_delete_empty_titles_and_bodies(self):
        ''' Test that verifies the dataframe do not contains empty titles and bodies '''
        df = pd.read_csv('articles_test.csv')
        pd_test.assert_frame_equal(df, delete_empty_titles_and_bodies(df))

    def test_clean_df_string(self):
        ''' Test that verifies the dataframe series do not contain the characters "['" and "']" '''
        logger.info('Starting test for the cleaning of the data.')
        df = pd.read_csv('articles_test.csv')
        df = clean_df_string(df)
        for data in df['title']:
            self.assertNotIn('[\'', data)
            self.assertNotIn('\']', data)
        for data in df['subtitle']:
            self.assertNotIn('[\'', data)
            self.assertNotIn('\']', data)
        for data in df['author']:
            self.assertNotIn('[\'', data)
            self.assertNotIn('\']', data)
        for data in df['category_long']:
            self.assertNotIn('[\'', data)
            self.assertNotIn('\']', data)
        for data in df['body']:
            self.assertNotIn('[\'', data)
            self.assertNotIn('\']', data)
        for data in df['tags']:
            self.assertNotIn('[\'', data)
            self.assertNotIn('\']', data)
        for data in df['images']:
            self.assertNotIn('[\'', data)
            self.assertNotIn('\']', data)
        pd_test.assert_frame_equal(df, clean_df_string(df))
    
    def test_clean_datetime(self):
        ''' Test that verifies that the publication date is a datetime type '''
        logger.info('Starting test for the datetime verification.')
        df = pd.read_csv('articles_test.csv')
        df = clean_df_string(df)
        df = clean_datetime(df)

        for date in df['publication_date']:
            self.assertEqual(type(date), type(today), msg='Not a datetime')

    def test_delete_first_space_categories(self):
        ''' Test that verifies the first character in categories, is not an empty space '''
        logger.info('Starting test that verifies that the first character in the categories, is not an empty space.')
        df = pd.read_csv('categories_test.csv')
        self.assertIsNotNone(delete_first_space_categories(df))
        df = delete_first_space_categories(df)
        for category in df['categories']:
            self.assertIsNot(category[0], '')

if __name__ == "__main__":
    unittest.main()