import pandas as pd
import plotly.express as px
import streamlit as st

# Cabeçalho do aplicativo
st.header("Análise de Anúncios de Vendas de Carros")

# Lendo os dados
car_data = pd.read_csv("vehicles_us.csv")

# Criando um botão para o histograma
hist_button = st.button("Criar histograma")

if hist_button:
  st.write("Criando um histograma para a coluna odometer")
  fig = px.histogram(car_data, x="odometer")
  st.plotly_chart(fig, use_container_width=True)

# Criando um botão para o gráfico de dispersão
scatter_button = st.button("Criar gráfico de dispersão")

if scatter_button:
  st.write("Criando um gráfico de dispersão entre odometer e price")
  fig_scatter = px.scatter(car_data, x="odometer", y="price")
  st.plotly_chart(fig_scatter, use_container_width=True)