import streamlit as st
import pandas as pd
import plotly.express as px

# Título de la aplicación
st.header("Análisis de Datos de Vehículos")

# Cargar el archivo CSV en un DataFrame
car_data = pd.read_csv('C:/Users/said2/Downloads/Repositorio/vehicles_us/vehicles_us.csv') # leer los datos

# Mostrar los primeros registros del conjunto de datos
st.write("Primeros registros del conjunto de datos:", car_data.head())

# Casilla de verificación para el histograma de precios
show_hist = st.checkbox('Mostrar Histograma de Precios')

# Casilla de verificación para el gráfico de dispersión
show_scatter = st.checkbox('Mostrar Gráfico de Dispersión (Precio vs Odometer)')

# Si el usuario selecciona la casilla del histograma
if show_hist:
    # Generar el histograma usando plotly express
    fig_hist = px.histogram(car_data, x="price", nbins=30, title="Distribución de Precios de Vehículos")
    
    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig_hist)

# Si el usuario selecciona la casilla del gráfico de dispersión
if show_scatter:
    # Generar el gráfico de dispersión usando plotly express
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Relación entre Odometer y Precio")
    
    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig_scatter)