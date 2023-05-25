import streamlit as st
import pandas as pd



# Charger les données à partir d'un fichier CSV
sales_data = pd.read_csv("sales_data.csv")

# Afficher les informations générales sur les données
st.write(sales_data.shape)
st.write(sales_data.dtypes)
st.write(sales_data.describe())


# Ajouter un filtre pour afficher les données par type de vente
sale_types = sales_data["SALE TYPE"].unique()
selected_sale_type = st.selectbox("Select a sale type", sale_types)
sale_type_data = sales_data[sales_data["SALE TYPE"] == selected_sale_type]
st.write(sale_type_data)
