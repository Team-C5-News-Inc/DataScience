import unittest
from extract import build_link, recover_text_file, categories_urls_extraction, articles_urls_extraction, articles_and_categories_extraction

class Test_Extract(unittest.TestCase):
    # Test Build links function
    
    def test_build_link(self):
        must_be_equal = ['https://www.vanguardia.com/area-metropolitana/giron/giron-acogera-la-ley-seca-y-el-toque-de-queda-para-halloween-CL3049224', 'https://noticias.canalrcn.com/nacional/tormenta-eta-genera-afectaciones-en-la-costa-caribe-colombiana-365083', 'https://www.ntn24.com/internacional/espana/segunda-noche-de-disturbios-en-espana-por-restricciones-contra-el-covid-19-0']
        links = ['/area-metropolitana/giron/giron-acogera-la-ley-seca-y-el-toque-de-queda-para-halloween-CL3049224', 'nacional/tormenta-eta-genera-afectaciones-en-la-costa-caribe-colombiana-365083', '/internacional/espana/segunda-noche-de-disturbios-en-espana-por-restricciones-contra-el-covid-19-0']
        host = ['https://www.vanguardia.com', 'https://noticias.canalrcn.com', 'https://www.ntn24.com', 'https://www.eluniversal.com.mx', 'https://www.eleconomista.com.mx', 'https://actualidad.rt.com']
        response = build_link(host, links)

        self.assertEqual(response, must_be_equal[0])


if __name__ == "__main__":
    unittest.main()