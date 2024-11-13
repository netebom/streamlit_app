import streamlit as st
import pandas as pd
import pyodbc
from dotenv import dotenv_values

st.title("👁️Welcome to the Data page")
st.write("Here you can view the data. Add your data viewing functionality here.")

# Load environment variables from .env file
env_vars = dotenv_values('.env')

# Connect to SQL Server using credentials from .env file
conn = pyodbc.connect(
    f"DRIVER={env_vars['DRIVER']};"
    f"SERVER={env_vars['SERVER']};"
    f"DATABASE={env_vars['DATABASE']};"
    f"UID={env_vars['UID']};"
    f"PWD={env_vars['PWD']};"
)

# Query the data
query = "SELECT * FROM dbo.LP2_Telco_churn_first_3000"
df = pd.read_sql(query, conn)

# Display data
st.write(df)

# Close the connection
conn.close()