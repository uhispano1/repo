import streamlit as st
import mysql.connector
import pandas as pd
import plotly.express as px

# Database connection

def get_db_connection():
    return mysql.connector.connect(
        host='sql3.freesqldatabase.com',
        user='sql3718601',
        password='XVdeEw7sCw',
        database='sql3718601'
    )

# Query to retrieve data
def fetch_data():
    conn = get_db_connection()
    query = "SELECT * FROM tableau_analytics"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Main function
def main():
    st.title('Sakila Results Analysis')
    
    # Fetch data
    df = fetch_data()
    
    # Display data
    st.write('### Sakila Results Data', df)
    
    # Plotting a graph using Plotly
    st.write('### Penalty Distribution')
    fig = px.histogram(df, x='Penalty', nbins=20, title='Penalty Distribution')
    st.plotly_chart(fig)
    
    # You can add more plots and analyses as needed
    
if __name__ == '__main__':
    main()
