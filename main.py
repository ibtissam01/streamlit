import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans

# Charger les données à partir d'un fichier CSV
sales_data = pd.read_csv("sales_data.csv")

# Afficher les informations générales sur les données
st.write("Informations générales sur les données :")
st.write(sales_data.shape)
st.write(sales_data.dtypes)
st.write(sales_data.describe())

# Créer une visualisation d'histogramme pour la distribution des quantités vendues
st.write("Distribution des quantités vendues :")
fig, ax = plt.subplots()
sns.histplot(sales_data["QUANTITY"], ax=ax)
st.pyplot(fig)

# Créer une visualisation de nuage de points pour la relation entre la quantité et le prix de vente
st.write("Relation entre la quantité et le prix de vente :")
fig, ax = pltDésolé, il semble que j'ai accidentellement envoyé une réponse incomplète. Voici la suite de ma réponse :
