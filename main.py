import streamlit as st
import pandas as pd
from st_files_connection import FilesConnection

conn = st.connection('s3', type=FilesConnection)
df = conn.read("atommych-datalake-dev/input/idealista/pt/braga/sale/homes/2024-01-19/pt_braga_sale_homes_2024-01-19.csv", input_format="csv", ttl=600)

st.write(df)