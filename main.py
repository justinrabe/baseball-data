import pandas as pd
import requests
from zipfile import ZipFile
import io


def extract_csv_from_zip (filename, myzip):
    with myzip.open(filename) as myfile:
        return pd.read_csv(myfile)
        
url = 'https://github.com/chadwickbureau/baseballdatabank/archive/refs/tags/v2022.2.zip'

response = requests.get(url,  stream=True, verify=False)
with ZipFile(io.BytesIO(response.content)) as myzip:
    df_pitching = extract_csv_from_zip('baseballdatabank-2022.2/core/Pitching.csv',myzip)
    df_appearances = extract_csv_from_zip('baseballdatabank-2022.2/core/Appearances.csv',myzip)
    df_batting = extract_csv_from_zip('baseballdatabank-2022.2/core/Batting.csv',myzip)
    df_batting_post = extract_csv_from_zip('baseballdatabank-2022.2/core/BattingPost.csv',myzip)
    df_Fielding = extract_csv_from_zip('baseballdatabank-2022.2/core/Fielding.csv',myzip)
    df_FieldingOF = extract_csv_from_zip('baseballdatabank-2022.2/core/FieldingOF.csv',myzip)
    df_FieldingOFsplit = extract_csv_from_zip('baseballdatabank-2022.2/core/FieldingOFsplit.csv',myzip)


