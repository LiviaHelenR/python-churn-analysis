import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Dashboard de Cancelamento de Clientes")

tabela = pd.read_csv("clientes.csv")

st.subheader("Visualização dos dados")
st.dataframe(tabela)

cancelamento = tabela["cancelou"].value_counts()

fig1 = px.bar(
    cancelamento,
    title="Clientes que cancelaram vs ativos"
)

st.plotly_chart(fig1)

fig2 = px.histogram(
    tabela,
    x="idade",
    color="cancelou",
    title="Cancelamento por idade"
)

st.plotly_chart(fig2)

fig3 = px.bar(
    tabela,
    x="plano",
    color="cancelou",
    title="Cancelamento por plano"
)

st.plotly_chart(fig3)