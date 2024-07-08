import streamlit as st
import pymysql
import pandas as pd
import matplotlib.pyplot as plt

# Database connection
def get_db_connection():
    return pymysql.connect(
        host='sql3.freesqldatabase.com',
        user='sql3718581',
        password='SjRPyzyhzc',
        db='sql3718581',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
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
    
    # Plotting a graph
    st.write('### Penalty Distribution')
    fig, ax = plt.subplots()
    df['Penalty'].hist(ax=ax, bins=20)
    ax.set_title('Penalty Distribution')
    ax.set_xlabel('Penalty')
    ax.set_ylabel('Frequency')
    st.pyplot(fig)
    
    # You can add more plots and analyses as needed
    
if __name__ == '__main__':
    main()
