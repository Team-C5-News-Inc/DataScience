import os.path
import pandas as pd


def main(file):
    file = pd.read_csv(file)
    print(file)

if __name__ == "__main__":
    if os.path.isfile('articles.csv'):
        main('articles.csv')