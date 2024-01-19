import streamlit as st
import pandas as pd
from pyathena import connect

# Initialize connection to db

@st.cache_resource
def init_connection():
    #url: str = st.secrets['supabase_url']
    #key: str = st.secrets['supabase_key']
    #connection = connect(s3_staging_dir="s3://atommych-datalake-dev/staging/streamlit/", region_name="eu-west-3")
    connection = connect(schema_name="datalake_raw", work_group="atommych-athena-workgroup-dev", profile_name="personal", region_name="eu-west-3")
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