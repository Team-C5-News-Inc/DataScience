import logging
logging.basicConfig(level=logging.INFO)
import subprocess

logger = logging.getLogger(__name__)


def _extract():
    subprocess.run(['python3', 'test_extract.py'], cwd='./extract')

def main():
    _extract()

if __name__ == "__main__":
    main()