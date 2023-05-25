import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Charger les données à partir d'un fichier CSV
sales_data = pd.read_csv("https://raw.githubusercontent.com/ibtissam01/streamlit/main/sales_data.csv")

# Afficher les informations générales sur les données
st.write(sales_data.shape)
st.write(sales_data.dtypes)
st.write(sales_data.describe())
st.pyplot(sns.scatterplot(x="QUANTITY", y="DISCOUNT %", data=sales_data)
# Ajouter un filtre pour afficher les données par type de vente
sale_types = sales_data["SALE TYPE"].unique()
selected_sale_type = st.selectbox("Select a sale type", sale_types)
sale_type_data = sales_data[sales_data["SALE TYPE"] == selected_sale_type]
st.write(sale_type_data)
