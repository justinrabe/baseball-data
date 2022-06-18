import pandas as pd
import requests
from zipfile import ZipFile
from sqlalchemy import create_engine
import io

##engine = create_engine('')

def extract_csv_from_zip (filename, myzip):
    with myzip.open(filename) as myfile:
        return pd.read_csv(myfile, nrows = 100)
        
url = 'https://github.com/chadwickbureau/baseballdatabank/archive/refs/tags/v2022.2.zip'

## potential to do: write a loop that grabs every CSV from the core folder and converts to SQL schema
response = requests.get(url,  stream=True, verify=False)
with ZipFile(io.BytesIO(response.content)) as myzip:
    df_pitching = extract_csv_from_zip('baseballdatabank-2022.2/core/Pitching.csv',myzip)
    df_appearances = extract_csv_from_zip('baseballdatabank-2022.2/core/Appearances.csv',myzip)
    df_batting = extract_csv_from_zip('baseballdatabank-2022.2/core/Batting.csv',myzip)
    df_batting_post = extract_csv_from_zip('baseballdatabank-2022.2/core/BattingPost.csv',myzip)
    df_Fielding = extract_csv_from_zip('baseballdatabank-2022.2/core/Fielding.csv',myzip)
    df_FieldingOF = extract_csv_from_zip('baseballdatabank-2022.2/core/FieldingOF.csv',myzip)
    df_FieldingOFsplit = extract_csv_from_zip('baseballdatabank-2022.2/core/FieldingOFsplit.csv',myzip)

print(pd.io.sql.get_schema(df_pitching, name = 'pitching_data'))
## perform insert into SQL DB
## perform data transforms
