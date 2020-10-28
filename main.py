import os.path
import logging
logging.basicConfig(level=logging.INFO)
import subprocess

logger = logging.getLogger(__name__)


def _extract():
    logger.info('Starting extract process')
    subprocess.run(['python3', 'extract.py'], cwd='./extract')

    subprocess.run(['find', '.', '-name', '{}'.format('articles.csv'), '-exec', 'mv', '{}', '../transform/{}'.format('articles.csv'), ';'], cwd='./extract')
    subprocess.run(['find', '.', '-name', '{}'.format('categories.csv'), '-exec', 'mv', '{}', '../transform/{}'.format('categories.csv'), ';'], cwd='./extract')

def _transform():
    logger.info('Starting transformation process...')
    subprocess.run(['python3', 'transform.py'], cwd='./transform')

    subprocess.run(['find', '.', '-name', '{}'.format('clean_articles.csv'), '-exec', 'mv', '{}', '../load/{}'.format('clean_articles.csv'), ';'], cwd='./transform')
    subprocess.run(['find', '.', '-name', '{}'.format('clean_categories.csv'), '-exec', 'mv', '{}', '../load/{}'.format('clean_categories.csv'), ';'], cwd='./transform')

def _load():
    logger.info('Starting load process...')
    subprocess.run(['python3', 'load.py'], cwd='./load')


def main():
    _extract()
    _transform()
    _load()

if __name__ == '__main__':
    main()