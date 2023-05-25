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

# Convertir la colonne de date en un type de données de date
sales_data["DATE"] = pd.to_datetime(sales_data["DATE"], format="%m/%d/%Y")

# Regrouper les données de ventes par date et calculer la somme de la quantité vendue pour chaque jour
daily_sales = sales_data.groupby("DATE").sum()["QUANTITY"]

# Créer un graphique de ligne de la quantité vendue en fonction de la date
fig, ax = plt.subplots()
ax.plot(daily_sales.index, daily_sales.values)
ax.set_xlabel("Date")
ax.set_ylabel("Quantité vendue")
ax.set_title("Évolution de la quantité vendue au fil du temps")
st.pyplot(fig)
# Regrouper les données de ventes par année et calculer la somme de la quantité vendue pour chaque année
yearly_sales = sales_data.groupby(sales_data["DATE"].dt.year)["QUANTITY"].sum()
# Créer un graphique à barres de la quantité de ventes par an
fig, ax = plt.subplots()
ax.bar(yearly_sales.index, yearly_sales.values)
ax.set_xlabel("Année")
ax.set_ylabel("Quantité vendue")
ax.set_title("Quantité de ventes par an")
st.pyplot(fig)
# Créer un graphique circulaire de la quantité de ventes par an
fig, ax = plt.subplots()
ax.pie(yearly_sales.values, labels=yearly_sales.index, autopct="%1.1f%%")
ax.set_title("Quantité de ventes par an")
st.pyplot(fig)
# Regrouper les données de ventes par mois et calculer la somme de la quantité vendue pour chaque mois
monthly_sales = sales_data.groupby(sales_data["DATE"].dt.strftime("%B %Y")).sum()["QUANTITY"]

# Créer un graphique à barres de la quantité de ventes par mois
fig, ax = plt.subplots()
ax.bar(monthly_sales.index, monthly_sales.values)
ax.set_xlabel("Mois")
ax.set_ylabel("Quantité vendue")
ax.set_title("Quantité de ventes par mois")
st.pyplot(fig)

# Créer une visualisation de nuage de points pour la relation entre la quantité et le prix de vente
'''st.write("Relation entre la quantité et le prix de vente :")
fig, ax = plt.subplots()
sns.scatterplot(x="QUANTITY", y="PRICE", data=sales_data, ax=ax)
st.pyplot(fig)

st.write("Modèle de régression linéaire pour prédire les ventes futures :")
X = sales_data[["QUANTITY"]]
y = sales_data["SALES"]
model = LinearRegression()
model.fit(X, y)
quantity_input = st.number_input("Entrez la quantité vendue :", min_value=0, max_value=10000)
predicted_sales = model.predict([[quantity_input]])
st.write("Les ventes prévues pour la quantité vendue sont de :", predicted_sales)
st.write("Modèle de clustering pour identifier les meilleures ventes :")
X = sales_data[["QUANTITY", "PRICE"]]
model = KMeans(n_clusters=3)
model.fit(X)
sales_data["cluster"] = model.predict(X)
st.write(sales_data.groupby("cluster").mean())'''
