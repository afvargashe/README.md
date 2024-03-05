#Realicé este proyecto con el fin de poner en práctica mis habilidades en python, puntualmente con la librería steamlit mediante la cual, desarrollé una aplicación web cuyo fin es crear un tablero interactivo que permite construir un histograma y un gráfico de dispersión sobre el comportamiento del kilometraje de diferentes automóviles dependiendo de si se marca o no cada casilla.

import streamlit as st
import pandas as pd
import plotly_express as px
df = pd.read_csv('C:\\Users\\ANDRES VARGAS\\Documents\\TRIPLETEN\\Sprints\\5. Sprint 5\\Proyecto\\README.md\\vehicles_us.csv')
st.header('Informe de venta de automóviles')
build_histogram = st.checkbox("Construir un histograma")
if build_histogram:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de automóviles')
    fig_hist = px.histogram(df, x='odometer')
    st.plotly_chart(fig_hist, use_container_width=True)
build_scatter_plot = st.checkbox("Construir un gráfico de dispersión")
if build_scatter_plot:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de automóviles')
    fig_disp = px.scatter(df, x='odometer')
    st.plotly_chart(fig_disp)