import streamlit as st
import mysql.connector
import pandas as pd
import plotly.express as px
import pyodbc


def fetch_data(sql):
    # Datos de conexión a SQL Server
    host = '13.67.133.149'
    database = 'Demo'  # Reemplaza con el nombre de tu base de datos
    user = 'streamlit'
    password = 'uhispano2024#'
    driver = '{ODBC Driver 17 for SQL Server}'  # Asegúrate de tener el driver correcto
    
    # Crear la cadena de conexión para SQL Server
    connection_string = f'DRIVER={driver};SERVER={host};DATABASE={database};UID={user};PWD={password}'
    
    # Conectar a la base de datos SQL Server
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    
    # Ejecutar una consulta
    cursor.execute(sql)
    
    # Obtener los nombres de las columnas
    columns = [column[0] for column in cursor.description]
    
    # Traer todos los resultados de la consulta
    result = [list(row) for row in cursor.fetchall()]
    # Crear el DataFrame a partir de los resultados
    df = pd.DataFrame(result, columns=columns)
    
    cursor.close()
    conn.close()
    return df

# Main function
def main():
    st.title('SQL Server Results Analysis')
    
    # Fetch data
    df = fetch_data("SELECT * FROM Person;")
    
    # Plotting a graph using Plotly
    st.write('### Person Distribution')
    fig = px.histogram(df, x='EmailPromotion', nbins=20, title='Person Distribution')
    st.plotly_chart(fig)

     # Fetch data
    df = fetch_data("SELECT top 10 * FROM Person;")
    
    # Display data
    st.write('### Person Results Data', df)

    # You can add more plots and analyses as needed
    
if __name__ == '__main__':
    main()
