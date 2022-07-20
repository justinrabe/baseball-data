# baseball-data
baseball data related project.

Step 1: 

Find a good data source. Currently looking for either a CSV based DS or API. 

Pandas will ingest the data into pandas DataFrames. I will then take the columns and turn it into schemas. 

Pandas might be too slow for these large datasets. I will need to use something different

I can spin up a quick Flask website for visualization.

I can develop my own RESTful APIs with Flask to pull data from SQL.
    https://auth0.com/blog/developing-restful-apis-with-python-and-flask/

Build a DWH in PostGresSQL first. Then I want to migrate that DWH to the cloud. Possible choices are Google BigQuery, AWS Redshift, etc.

# docker run -it \
#   -e POSTGRES_USER="root" \
#   -e POSTGRES_PASSWORD="root" \
#   -e POSTGRES_DB="baseball_data" \
#   -v c:/Users/Justin/Documents/Git/baseball-data/baseball_data_volume:/var/lib/postgresql/data \
#   -p 5432:5432 \
#  postgres:13

docker run -it -e POSTGRES_USER="root" -e POSTGRES_PASSWORD="root" -e POSTGRES_DB="baseball_data" -v c:/Users/Justin/Documents/Git/baseball-data/baseball_data_volume:/var/lib/postgresql/data -p 5432:5432 postgres:13
