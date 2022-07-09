import pandas as pd
import argparse
import requests
from zipfile import ZipFile
from sqlalchemy import create_engine
import io

url = 'https://github.com/chadwickbureau/baseballdatabank/archive/refs/tags/v2022.2.zip'

def main(params):
    print(params)
    user = params.user
    password = params.password
    host = params.host 
    port = params.port 
    ##table_name = params.table_name
    ##engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    response = requests.get(url,  stream=True, verify=False)
    with ZipFile(io.BytesIO(response.content)) as myzip:
        df_pitching = extract_csv_from_zip('baseballdatabank-2022.2/core/Pitching.csv',myzip)
        df_appearances = extract_csv_from_zip('baseballdatabank-2022.2/core/Appearances.csv',myzip)
        df_batting = extract_csv_from_zip('baseballdatabank-2022.2/core/Batting.csv',myzip)
        df_batting_post = extract_csv_from_zip('baseballdatabank-2022.2/core/BattingPost.csv',myzip)
        df_Fielding = extract_csv_from_zip('baseballdatabank-2022.2/core/Fielding.csv',myzip)
        df_FieldingOF = extract_csv_from_zip('baseballdatabank-2022.2/core/FieldingOF.csv',myzip)
        df_FieldingOFsplit = extract_csv_from_zip('baseballdatabank-2022.2/core/FieldingOFsplit.csv',myzip)

    ##df_pitching.to_sql(name="pitching", con = engine, if_exists='append', chunksize=1000)

def extract_csv_from_zip (filename, myzip):
    with myzip.open(filename) as myfile:
        return pd.read_csv(myfile, nrows = 100) ## limiting to 100 rows for faster testing
        

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest data to Postgres')

    parser.add_argument('--user', required=True, help='user name for postgres')
    parser.add_argument('--password', required=True, help='password for postgres')
    parser.add_argument('--host', required=True, help='host for postgres')
    parser.add_argument('--port', required=True, help='port for postgres')

    args = parser.parse_args()

    main(args)
## potential to do: write a loop that grabs every CSV from the core folder and converts to SQL schema


##print(pd.io.sql.get_schema(df_pitching, name = 'pitching_data'))
## perform insert into SQL DB
## perform data transforms
## need to draft up ETL ideas, error checking
