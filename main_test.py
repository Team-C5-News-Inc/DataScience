import subprocess

# Salute to Edward Toledo [C4], for enlight me with the use of tests.

def _extract():
    subprocess.run(['python3', 'test_extract.py'], cwd='./extract')

def _transform():
    subprocess.run(['python3', 'test_transform.py'], cwd='./transform')

def _load():
    subprocess.run(['python3', 'test_load.py'], cwd='./load')

def main():
    _extract()
    _transform()
    _load()

if __name__ == "__main__":
    main()