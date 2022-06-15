import pandas as pd
import requests
from zipfile import ZipFile
import io


def extract_csv_zip (filename, myzip):
    with myzip.open(filename) as myfile:
        return pd.read_csv(myfile)

## TODO Parameterize CSV to grab each CSV. The Function should take the file name as input and output a pandas DF
url = 'https://github.com/chadwickbureau/baseballdatabank/archive/refs/tags/v2022.2.zip'

response = requests.get(url,  stream=True, verify=False)
with ZipFile(io.BytesIO(response.content)) as myzip:
    df = extract_csv_zip('baseballdatabank-2022.2/core/Pitching.csv',myzip)

print(df)

