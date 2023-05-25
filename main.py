import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.cluster import KMeans
from sklearn.metrics import r2_score, silhouette_score
import streamlit as st

# Charger le fichier Excel dans un DataFrame Pandas
df = pd.read_excel('sales_data.xlsx')

# Analyse de données exploratoire
st.title('Sales Dashboard')
st.write('## Data Exploration')

# Afficher les premières lignes du DataFrame
if st.checkbox('Show Data'):
    st.write(df.head())

# Afficher les statistiques descriptives des données
if st.checkbox('Show Descriptive Statistics'):
    st.write(df.describe())

# Afficher un graphique en boîte de la quantité de vente
df.boxplot(column='Quantity', vert=False)
plt.title('Quantity Boxplot')
plt.xlabel('Quantity')
st.pyplot()

# Afficher un graphique en boîte du pourcentage de réduction
df.boxplot(column='Discount %', vert=False)
plt.title('Discount Boxplot')
plt.xlabel('Discount%')
st.pyplot()

# Afficher une matrice de corrélation des variables
corr_matrix = df.corr()
sns.heatmap(corr_matrix, annot=True)
st.pyplot()

# Modèles de régression pour prédire les ventes futures
st.write('## Sales Prediction')

# Préparation des données pour la régression linéaire
X = df[['Quantity', 'Discount %']]
y = df['SALE TYPE']

# Création des modèles de régression
models = {'Linear Regression': LinearRegression(),
          'Decision Tree Regression': DecisionTreeRegressor(),
          'Random Forest Regression': RandomForestRegressor()}

# Entraînement des modèles et calcul de l'accuracy
for name, model in models.items():
    model.fit(X, y)
    y_pred = model.predict(X)
    r2 = r2_score(y, y_pred)
    st.write(f'{name} Accuracy:', r2)

# Modèles de clustering pour segmenter les clients
st.write('## Customer Segmentation')

# Préparation des données pour le clustering
X = df[['Quantity', 'Discount %']]

# Création des modèles de clustering
models = {'K-Means Clustering (k=2)': KMeans(n_clusters=2),
          'K-Means Clustering (k=3)': KMeans(n_clusters=3),
          'K-Means Clustering (k=4)': KMeans(n_clusters=4)}

# Entraînement des modèles et calcul de l'accuracy
for name, model in models.items():
    model.fit(X)
    y_pred = model.predict(X)
    silhouette = silhouette_score(X, y_pred)
    st.write(f'{name} Silhouette Score:', silhouette)

# Interface utilisateur Streamlit pour l'application
st.write('## Sales Dashboard Application')
st.write('Enter the sales data below to see the predicted sales type for the given quantity and discount.')

# Afficher un formulaire pour saisir les données de vente
form = st.form(key='my_form')
quantity = form.number_input('Quantity', min_value=0)
discount = form.number_input('Discount %', min_value=0, max_value=100)
submit_button = form.form_submit_button(label='Submit')

# Prédire le type de vente en fonction des données de vente saisies
if submit_button:
    new_data = {'Quantity': quantity, 'Discount %': discount}
    X_new = pd.DataFrame(new_data, index=[0])
    for name, model in models.items():
        y_new = model.predict(X_new)
        st.write(f'Predicted sales type for {quantity} quantity and {discount}% discount using {name}:', y_new[0])
