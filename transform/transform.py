import os.path
import pandas as pd

def _delete_empty_titles(df):
    for index in range(len(df)):
        if df['title'][index] == '[]':
            df.drop([index], axis = 0, inplace = True)
    return df

def main(file):
    df = pd.read_csv(file)
    df = _delete_empty_titles(file)
    print(df)

if __name__ == "__main__":
    main('articles.csv')
    