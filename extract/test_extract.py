import unittest
import logging
logging.basicConfig(level=logging.INFO)
from extract import build_link, recover_text_file, categories_urls_extraction, articles_urls_extraction, articles_and_categories_extraction

logger = logging.getLogger(__name__)


HOST = ['https://www.vanguardia.com', 'https://noticias.canalrcn.com', 'https://www.ntn24.com', 'https://www.eluniversal.com.mx', 'https://www.eleconomista.com.mx', 'https://actualidad.rt.com']
class Test_Extract(unittest.TestCase):
    # Test Build links function
    logger.info('Starting test for the data extraction.')
    def test_build_link(self):
        ''' Test that verifies if a link is well formed '''
        logger.info('Starting build link test')
        must_be_equal = ['https://www.vanguardia.com/area-metropolitana/giron/giron-acogera-la-ley-seca-y-el-toque-de-queda-para-halloween-CL3049224', 'https://noticias.canalrcn.com/nacional/tormenta-eta-genera-afectaciones-en-la-costa-caribe-colombiana-365083', 'https://www.ntn24.com/internacional/espana/segunda-noche-de-disturbios-en-espana-por-restricciones-contra-el-covid-19-0', 'https://www.eluniversal.com.mx/mundo/estados-unidos-llega-elecciones-con-fractura-en-su-sistema-politico', 'https://www.eleconomista.com.mx/empresas/Inversion-historica-de-las-companias-alemanas-en-Mexico-20201101-0005.html', 'https://actualidad.rt.com/actualidad/371802-italia-aterradores-datos-coronavirus-nuevas-restricciones']
        links = ['/area-metropolitana/giron/giron-acogera-la-ley-seca-y-el-toque-de-queda-para-halloween-CL3049224', 'nacional/tormenta-eta-genera-afectaciones-en-la-costa-caribe-colombiana-365083', '/internacional/espana/segunda-noche-de-disturbios-en-espana-por-restricciones-contra-el-covid-19-0', '/mundo/estados-unidos-llega-elecciones-con-fractura-en-su-sistema-politico', '/empresas/Inversion-historica-de-las-companias-alemanas-en-Mexico-20201101-0005.html', '/actualidad/371802-italia-aterradores-datos-coronavirus-nuevas-restricciones']
        
        response = []
        for i in range(len(HOST)):
            response.append(build_link(HOST[i], links[i]))
            self.assertEqual(response[i], must_be_equal[i])

    def test_recover_text_file(self):
        ''' Test that verifies if the urls articles and categories are recovered '''
        logger.info('Starting test for data persistence in urls and categories')
        url = []
        file = open('urls.txt', 'r')
        for line in file:
            link = line.rstrip('\\n')
            link = link.replace('\n', '')
            url.append(link)
        file.close()
        self.assertEqual(url, recover_text_file('urls.txt'))

        categories = []
        file = open('categories.txt', 'r')
        for line in file:
            category = line.rstrip('\\n')
            category = line.replace('\n', '')
            categories.append(category)
        file.close()
        self.assertEqual(categories, recover_text_file('categories.txt'))

    def test_categories_urls_extraction(self):
        ''' Test that verifies that the categories are recovered from the host '''
        logger.info('Starting test for categories url extraction')
        for iterator in range(len(HOST)):
            self.assertIsNotNone(categories_urls_extraction(HOST[iterator], iterator))

    def test_articles_url_extraction(self):
        ''' Test that verifies if the url articles are extracted from the categories url list '''
        logger.info('Starting test for articles url extraction')
        for iterator in range(len(HOST)):
            categories = categories_urls_extraction(HOST[iterator], iterator)
            self.assertIsNotNone(articles_urls_extraction(HOST[iterator], categories, iterator))
        

    def test_articles_and_categories_extraction(self):
        ''' Test that verifies if the article and category are extracted from the articles url list '''
        logger.info('Starting test for articles and categories extraction')
        for iterator in range(len(HOST)):
            categories = categories_urls_extraction(HOST[iterator], iterator)
            articles = articles_urls_extraction(HOST[iterator], categories, iterator)
            for article in articles:
                self.assertIsNotNone(articles_and_categories_extraction(HOST[iterator], article, iterator))

if __name__ == "__main__":
    unittest.main()