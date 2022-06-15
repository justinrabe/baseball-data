import pandas as pd
import requests
from zipfile import ZipFile
import io

# Example dataset

## TODO Parameterize CSV to grab each CSV. The Function should take the file name as input and output a pandas DF
url = 'https://github.com/chadwickbureau/baseballdatabank/archive/refs/tags/v2022.2.zip'

response = requests.get(url,  stream=True, verify=False)
with ZipFile(io.BytesIO(response.content)) as myzip:
    print(myzip)
    print(myzip.namelist())
    with myzip.open('baseballdatabank-2022.2/core/Pitching.csv') as myfile:
        df = pd.read_csv(myfile)

print(df)