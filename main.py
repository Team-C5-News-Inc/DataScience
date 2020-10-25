import os.path
import logging
logging.basicConfig(level=logging.INFO)
import subprocess

logger = logging.getLogger(__name__)


def _extract():
    logger.info('Starting extract process')
    subprocess.run(['python3', 'extract.py'], cwd='./extract')

    subprocess.run(['find', '.', '-name', '{}'.format('articles.csv'), '-exec', 'mv', '{}', '../transform/{}'.format('articles.csv'), ';'], cwd='./extract')
    subprocess.run(['find', '.', '-name', '{}'.format('articles.csv'), '-exec', 'mv', '{}', '../transform/{}'.format('articles.csv'), ';'], cwd='./extract')

    subprocess.run(['find', '.', '-name', '{}'.format('categories.csv'), '-exec', 'mv', '{}', '../transform/{}'.format('categories.csv'), ';'], cwd='./extract')
    subprocess.run(['find', '.', '-name', '{}'.format('categories.csv'), '-exec', 'mv', '{}', '../transform/{}'.format('categories.csv'), ';'], cwd='./extract')
        

def main():
    _extract()


if __name__ == '__main__':
    main()
    