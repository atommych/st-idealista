import streamlit as st
import pandas as pd
from pyathena import connect
import os
# Initialize connection to db

@st.cache_resource
def init_connection():
    #connection = connect(s3_staging_dir="s3://atommych-datalake-dev/staging/streamlit/", region_name="eu-west-3")
    #connection = connect(schema_name="datalake_raw", work_group="atommych-athena-workgroup-dev", profile_name="personal", region_name="eu-west-3")

    # Get environment variables
    access_key = os.getenv('access_key')
    secret_key = os.environ.get('secret_key')
    region = os.environ.get('region')
    s3_staging_dir = os.environ.get('s3_staging_dir')
    connection = connect(aws_access_key_id=secret_key,
                     aws_secret_access_key=access_key,
                     s3_staging_dir=s3_staging_dir,
                     region_name=region)
    return connection

# Query the db
@st.cache_data(ttl=600)  # cache clears after 10 minutes
def run_query():
    # Return all data
    df = pd.read_sql("select * from idealista_braga_sale_homes", connection)
    return df

connection = init_connection()
rows = run_query()
st.write(rows)