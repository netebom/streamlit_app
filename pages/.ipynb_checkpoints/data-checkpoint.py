import streamlit as st
import pandas as pd
from urllib.parse import quote_plus
import os
import pyodbc
from dotenv import dotenv_values, load_dotenv

# Set up page title
st.set_page_config(
    page_title="View Data",
    page_icon="📊",
    layout="wide"
)

# Title and description
st.title("👁️ Welcome to the Data Page")
st.write("Here you can view the data fetched from your database.")

# Load environment variables from .env file
# env_vars = dotenv_values('.env')

# Initialize the connection variable
conn = None
# env_vars = {'SERVER': 'dap-projects-database.database.windows.net', 'USER': 'LP2_project', 'PASSWORD': 'Stat$AndD@t@Rul3', 'DATABASE': 'dapDB'}
try:
    # Establish database connection using credentials from .env file
    load_dotenv()

    # Getting environment variables
    server = os.getenv("SERVER")
    database = os.getenv("DATABASE")
    username = os.getenv("USER")
    password = os.getenv("PASSWORD")

    # URL-encode password to handle special characters
    encoded_password = quote_plus(password)

    # SQLAlchemy connection string
    # connection_string = f"mssql+pyodbc://{username}:{encoded_password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server"

    # server = env_vars.get('SERVER')
    # database = env_vars.get('DATABASE')
    # username = env_vars.get('USER')
    # password = env_vars.get('PASSWORD')
   
    connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};MARS_Connection=yes;MinProtocolVersion=TLSv1.2;"

    conn = pyodbc.connect(connection_string)
    st.success("Successfully connected to the database!")

    # SQL query to fetch data
    query = "SELECT * FROM dbo.LP2_Telco_churn_first_3000"
    df = pd.read_sql(query, conn)

    # Display the data in a nice table
    st.write(df)

except Exception as e:
    st.error(f"Error: {e.__str__()}")

finally:
    # Close the connection if it was successfully opened
    if conn:
        conn.close()
        st.info("Database connection closed.")
