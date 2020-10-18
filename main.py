import logging
logging.basicConfig(level=logging.INFO)
import subprocess

logger = logging.getLogger(__name__)

news_sites_uids = [1]

def _extract():
    logger.info('Starting extract process')
    for news_sites_uid in news_sites_uids:
        subprocess.run(['python3', 'main.py', str(news_sites_uid)], cwd='./extract')


def main():
    _extract()


if __name__ == '__main__':
    main()
    